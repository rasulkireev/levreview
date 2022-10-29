from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

from djstripe.models import Customer, Price, Subscription
import djstripe.settings as djstripe_settings
import stripe

from .models import CustomUser
from .utils import add_users_context

stripe.api_key = djstripe_settings.djstripe_settings.STRIPE_SECRET_KEY

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = "account_login"
    model = CustomUser
    fields = ["first_name", "last_name", "email"]
    success_message = "User Profile Updated"
    success_url = reverse_lazy("dashboard")
    template_name = "account/settings.html"

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        add_users_context(context, self.request.user)

        return context

def create_checkout_session(request):
    user = request.user
    price_id = Price.objects.first().id
    customer = Customer.objects.get(subscriber=user)

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        customer=customer.id,
        line_items=[{
            "price": price_id,
            "quantity": 1,
        }],
        mode='subscription',
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
        event = stripe.Webhook.construct_event(
          payload,
          sig_header,
          settings.DJSTRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(e, status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(e, status=400)

    if event.type == "checkout.session.completed":

        subscription = Subscription.sync_from_stripe_data(
          stripe.Subscription.retrieve(event["data"]["object"]["subscription"])
        )

        print(subscription)
        # customer.subscribe(items=[{"price": price_1}, {"price": price_2}])

        # current_user = CustomUser.objects.get(pk=user_id)
        # current_user.subscription_level = "PRO"
        # current_user.save()

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