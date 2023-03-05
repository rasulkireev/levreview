import logging

from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.crypto import get_random_string

from levreview.utils import DivErrorList

from .models import CustomUser

logger = logging.getLogger(__file__)


class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)

        # Generate random username
        user.username = get_random_string(length=12)

        num = 1
        User = get_user_model()
        while User.objects.filter(username=user.username).exists():
            user.username = f"{get_random_string(length=10)}_{num}"
            num += 1

        return user


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList


class UpdateMinRatingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateMinRatingForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList

    min_rating = forms.ChoiceField(
        choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)),
        widget=forms.Select(),
    )

    class Meta:
        model = CustomUser
        fields = ["min_rating"]
