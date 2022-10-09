from django.forms import ModelForm

from .models import Location, Review

class CreateLocationForm(ModelForm):
    class Meta:
        model = Location
        fields = [
          "google_place_id",
          "name",
          "address",
          "phone_number"
        ]


class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
          "rating",
          "name",
          "email",
          "feedback"
        ]
