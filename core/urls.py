from django.urls import path

from .views import LocationDetailView, LocationCreateView, ReviewCreateView

urlpatterns = [
    path("create/", LocationCreateView.as_view(), name="create-location"),
    path("<str:google_place_id>/", LocationDetailView.as_view(), name="detail-location"),
    path("<str:google_place_id>/create", ReviewCreateView.as_view(), name="create-review"),
]
