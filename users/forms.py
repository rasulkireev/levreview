import logging

from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.forms import ModelForm

from levreview.utils import DivErrorList

from .models import CustomUser

logger = logging.getLogger(__file__)


class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList


class UpdateMinRatingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateMinRatingForm, self).__init__(*args, **kwargs)

        self.error_class = DivErrorList
        self.fields["min_rating"].initial = 3

    min_rating = forms.ChoiceField(
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)),
        widget=forms.Select(),
    )

    class Meta:
        model = CustomUser
        fields = ["min_rating"]
