from django.urls import path

from .views import (
    UserUpdateView,
    create_checkout_session,
    create_customer_portal_session,
    resend_email_confirmation_email,
    successfull_payment_webhook,
)

urlpatterns = [
    path("settings/", UserUpdateView.as_view(), name="settings"),
    path("create-checkout-session/", create_checkout_session, name="checkout"),
    path(
        "create-customer-portal-session/",
        create_customer_portal_session,
        name="create-customer-portal-session",
    ),
    path("webhook/", successfull_payment_webhook, name="webhook"),
    path(
        "send-confirmation",
        resend_email_confirmation_email,
        name="resend_email_confirmation_email",
    ),
]
