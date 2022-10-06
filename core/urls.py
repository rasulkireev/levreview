from django.urls import path

from .views import LocationDetailView, LocationCreateView

urlpatterns = [
    path("create/", LocationCreateView.as_view(), name="create-location"),
    path("<str:google_place_id>/", LocationDetailView.as_view(), name="location"),
]
