import djstripe.settings as djstripe_settings
import stripe
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import FormView, UpdateView
from djstripe.models import Customer, Price, Subscription

from .forms import UpdateMinRatingForm
from .models import CustomUser
from .utils import add_users_context

stripe.api_key = djstripe_settings.djstripe_settings.STRIPE_SECRET_KEY


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = "account_login"
    model = CustomUser
    fields = ["first_name", "last_name", "email"]
    success_message = "User Profile Updated"
    success_url = reverse_lazy("settings")
    template_name = "account/settings.html"

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["min_rating_form"] = UpdateMinRatingForm
        context["min_rating"] = user.location.first().min_rating

        add_users_context(context, user)

        return context


class UpdateMinRatingView(LoginRequiredMixin, FormView):
    login_url = "account_login"
    form_class = UpdateMinRatingForm
    success_url = reverse_lazy("settings")
    template_name = "account/min-rating-form.html"

    def form_valid(self, form):
        user = self.request.user
        user.location.all().update(min_rating=form.cleaned_data["min_rating"])

        return super(UpdateMinRatingView, self).form_valid(form)


def create_checkout_session(request):
    user = request.user
    price_id = Price.objects.get(nickname="monthly").id
    customer = Customer.objects.get(subscriber=user)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        customer=customer.id,
        line_items=[
            {
                "price": price_id,
                "quantity": 1,
            }
        ],
        mode="subscription",
        allow_promotion_codes=True,
        success_url=request.build_absolute_uri(reverse_lazy("settings")) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse_lazy("settings")) + "?status=failed",
        metadata={f"{djstripe_settings.djstripe_settings.SUBSCRIBER_CUSTOMER_KEY}": user.id},
    )

    return redirect(checkout_session.url, code=303)


@csrf_exempt
@require_POST
def successfull_payment_webhook(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.DJSTRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        return HttpResponse(e, status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(e, status=400)

    event_types = (
        "customer.subscription.created",
        "customer.subscription.updated",
        "customer.subscription.deleted",
    )

    if event["type"] in event_types:
        subscription_id = event["data"]["object"]["items"]["data"][0]["subscription"]
        Subscription.sync_from_stripe_data(stripe.Subscription.retrieve(subscription_id))

    return HttpResponse(status=200)


def create_customer_portal_session(request):
    customer = Customer.objects.get(subscriber=request.user)
    session = stripe.billing_portal.Session.create(
        customer=customer.id,
        return_url=request.build_absolute_uri(reverse_lazy("settings")),
    )

    return redirect(session.url)


def resend_email_confirmation_email(request):
    user = request.user
    send_email_confirmation(request, user, user.email)

    return redirect("settings")
