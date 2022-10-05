from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "pages/home.html"

class DashboardView(TemplateView):
    template_name = "pages/dashboard.html"