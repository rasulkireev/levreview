from django.db import models
from django.urls import reverse
from django.conf import settings
from model_utils.models import TimeStampedModel

class Location(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="location")
    google_place_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("location", kwargs={"google_place_id": self.google_place_id})