from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Location, Review
class HomeView(TemplateView):
    template_name = "pages/home.html"

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "pages/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = Location.objects.filter(owner=self.request.user)
        context["locations"] = locations
        context["reviews"] = Review.objects.filter(location__in=[location.id for location in locations])
        context["num_of_locations"] = len(locations)

        return context