from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Location, Review
from .forms import CreateLocationForm, CreateReviewForm

class LocationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Location
    form_class = CreateLocationForm
    template_name = "core/location-create.html"

    def get_success_url(self):
      return reverse("dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_of_locations"] = len(Location.objects.filter(owner=self.request.user))

        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()

        return super(LocationCreateView, self).form_valid(form)

class LocationDetailView(LoginRequiredMixin, DetailView):
    model = Location
    template_name = "core/location-detail.html"
    slug_field = 'google_place_id'
    slug_url_kwarg = 'google_place_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["num_of_locations"] = len(Location.objects.filter(owner=self.request.user))

        current_location = Location.objects.get(google_place_id = self.kwargs["google_place_id"])
        context["reviews"] = Review.objects.filter(location=current_location)

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