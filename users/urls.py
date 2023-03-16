from django.urls import path

from .views import (
    UpdateMinRatingView,
    UserUpdateView,
    create_checkout_session,
    create_customer_portal_session,
    resend_email_confirmation_email,
)

urlpatterns = [
    path("settings/", UserUpdateView.as_view(), name="settings"),
    path("create-checkout-session/", create_checkout_session, name="checkout"),
    path("update-min-rating/", UpdateMinRatingView.as_view(), name="update-min-rating"),
    path(
        "create-customer-portal-session/",
        create_customer_portal_session,
        name="create-customer-portal-session",
    ),
    path(
        "send-confirmation",
        resend_email_confirmation_email,
        name="resend_email_confirmation_email",
    ),
]
