import logging

from allauth.account.models import EmailAddress
from djstripe.models import Customer, Subscription

from core.models import Location

logger = logging.getLogger(__file__)


def add_users_context(context, user):
    try:
        customer = Customer.objects.get(subscriber=user)
        logger.info(f"Adding customer {customer} to context.")
        context["customer"] = customer

        try:
            subscription = Subscription.objects.get(customer=customer)
            logger.info(f"Adding subscription {subscription} to context.")
            context["subscription"] = subscription
        except Subscription.DoesNotExist as e:
            logger.error(f"Subscription Error: {e}")

    except Customer.DoesNotExist as e:
        logger.error(f"Customer Error: {e}")

    try:
        context["email_verified"] = EmailAddress.objects.get_for_user(user, user.email).verified
    except EmailAddress.DoesNotExist as e:
        logger.error(f"Email Error: {e}")

    locations = Location.objects.filter(owner=user)
    context["locations"] = locations

    return context
