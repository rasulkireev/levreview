from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from users.utils import add_users_context

from .forms import CreateLocationForm, CreateReviewForm
from .models import Location, Review


class LocationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = "account_login"
    model = Location
    form_class = CreateLocationForm
    template_name = "core/location-create.html"

    def get_success_url(self):
        return reverse("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_users_context(context, self.request.user)

        return context

    def form_valid(self, form):
        current_user = self.request.user

        form.instance.owner = current_user
        form.instance.min_rating = current_user.min_rating

        self.object = form.save()

        return super(LocationCreateView, self).form_valid(form)


class LocationDetailView(LoginRequiredMixin, DetailView):
    login_url = "account_login"
    model = Location
    template_name = "core/location-detail.html"
    slug_field = "google_place_id"
    slug_url_kwarg = "google_place_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_location = Location.objects.get(google_place_id=self.kwargs["google_place_id"])
        context["reviews"] = Review.objects.filter(location=current_location)
        add_users_context(context, self.request.user)

        return context


class ReviewCreateView(CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = "core/review-create.html"

    def get_success_url(self):
        return reverse("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = Location.objects.get(google_place_id=self.kwargs["google_place_id"])

        return context

    def form_valid(self, form):
        form.instance.location = Location.objects.get(google_place_id=self.kwargs["google_place_id"])
        self.object = form.save()

        return super(ReviewCreateView, self).form_valid(form)


class ReviewDetailView(LoginRequiredMixin, DetailView):
    login_url = "account_login"
    model = Review
    template_name = "core/review-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_users_context(context, self.request.user)

        return context
