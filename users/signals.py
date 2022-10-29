from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from djstripe.models import Customer

@receiver(email_confirmed)
def create_stripe_customer(**kwargs):
    user = get_user_model().objects.get(email=kwargs["email_address"])
    Customer.get_or_create(subscriber=user)