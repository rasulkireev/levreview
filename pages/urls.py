from django.urls import path

from .views import ContactView, DashboardView, HomeView, PrivacyView, TermsView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
    path("terms/", TermsView.as_view(), name="terms"),
    path("contact/", ContactView.as_view(), name="contact"),
]
