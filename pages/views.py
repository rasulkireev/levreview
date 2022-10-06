from django.views.generic import TemplateView

from core.models import Location
class HomeView(TemplateView):
    template_name = "pages/home.html"

class DashboardView(TemplateView):
    template_name = "pages/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = Location.objects.filter(owner=self.request.user)

        return context