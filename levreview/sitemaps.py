from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5

    def items(self):
        return ["home"]

    def location(self, item):
        return reverse(item)


sitemaps = {
    "static": StaticViewSitemap,
}
