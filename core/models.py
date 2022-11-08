from email.policy import default

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class Location(TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="location")
    google_place_id = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    min_rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.name}: {self.google_place_id}"

    def get_absolute_url(self):
        return reverse("detail-location", kwargs={"google_place_id": self.google_place_id})


class Review(TimeStampedModel):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="review")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse("create-review", kwargs={"google_place_id": self.google_place_id})
