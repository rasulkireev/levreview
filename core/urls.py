from django.urls import path

from .views import PlaceFinderView

urlpatterns = [
    path("", PlaceFinderView.as_view(), name="place-finder"),
]
