from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Location
from .forms import CreateLocationForm

class LocationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Location
    form_class = CreateLocationForm
    template_name = "core/location-create.html"

    def get_success_url(self):
      return reverse("dashboard")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()

        return super(LocationCreateView, self).form_valid(form)

class LocationDetailView(DetailView):
    model = Location
    template_name = "core/location-detail.html"