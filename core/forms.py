from django.forms import ModelForm

from .models import Location

class CreateLocationForm(ModelForm):
    class Meta:
        model = Location
        fields = [
          "google_place_id",
          "name",
          "address",
          "phone_number"
        ]
