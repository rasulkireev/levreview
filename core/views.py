from django.views.generic import TemplateView

class PlaceFinderView(TemplateView):
    template_name = "core/id_finder.html"