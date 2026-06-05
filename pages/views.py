import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from core.models import Location, Review
from users.utils import add_users_context

logger = logging.getLogger(__file__)


class HomeView(TemplateView):
    template_name = "pages/home.html"


class PrivacyView(TemplateView):
    template_name = "pages/privacy.html"


class TermsView(TemplateView):
    template_name = "pages/terms.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = "account_login"
    template_name = "pages/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        logger.debug(f"User: {user}")
        locations = Location.objects.filter(owner=user)

        context["locations"] = locations
        context["reviews"] = Review.objects.filter(location__in=[location.id for location in locations])
        add_users_context(context, user)

        return context
