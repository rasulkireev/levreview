from django.forms import Form, ModelForm

from levreview.utils import DivErrorList

from .models import Location, Review


class CreateLocationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateLocationForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList

    class Meta:
        model = Location
        fields = ["google_place_id", "name", "address", "phone_number", "min_rating"]


class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "name", "email", "feedback"]
