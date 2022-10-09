from django.contrib import admin

from .models import Location, Review

class LocationAdmin(admin.ModelAdmin):
    list_display = ("owner", "google_place_id", "name", "min_rating",)


admin.site.register(Location, LocationAdmin)
admin.site.register(Review)