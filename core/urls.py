from django.urls import path

from .views import LocationCreateView, LocationDetailView, ReviewCreateView, ReviewDetailView

urlpatterns = [
    path("create/", LocationCreateView.as_view(), name="create-location"),
    path("<str:google_place_id>/", LocationDetailView.as_view(), name="detail-location"),
    path("<str:google_place_id>/review", ReviewCreateView.as_view(), name="create-review"),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="detail-review"),
]
