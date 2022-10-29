from allauth.account.models import EmailAddress
from djstripe.models import Customer, Subscription
from core.models import Location

def add_users_context(context, user):
  try:
    customer = Customer.objects.get(subscriber=user)
    context["customer"] = customer

    try:
      context["subscription"] = Subscription.objects.get(customer=customer)
    except Subscription.DoesNotExist as e:
      print(f"Subscription Error: {e}")

  except Customer.DoesNotExist as e:
    print(f"Customer Error: {e}")

  locations = Location.objects.filter(owner=user)
  context["locations"] = locations
  context["email_verified"] = EmailAddress.objects.get_for_user(user, user.email).verified

  return context