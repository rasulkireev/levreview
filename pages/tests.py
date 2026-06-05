from django.contrib.sites.models import Site
from django.test import TestCase, override_settings
from django.urls import reverse


class SeoRouteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Site.objects.update_or_create(id=1, defaults={"domain": "levreview.com", "name": "Lev Review"})

    @override_settings(ALLOWED_HOSTS=["testserver"])
    def test_robots_txt_links_https_sitemap(self):
        response = self.client.get(reverse("robots"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/plain")
        self.assertContains(response, "Sitemap: https://levreview.com/sitemap.xml")

    @override_settings(ALLOWED_HOSTS=["levreview.com"])
    def test_sitemap_uses_https_urls(self):
        response = self.client.get("/sitemap.xml", secure=True, HTTP_HOST="levreview.com")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<loc>https://levreview.com/</loc>")
        self.assertContains(response, "<loc>https://levreview.com/privacy/</loc>")
        self.assertContains(response, "<loc>https://levreview.com/terms/</loc>")
        self.assertContains(response, "<loc>https://levreview.com/contact/</loc>")

    @override_settings(
        ALLOWED_HOSTS=["levreview.com", "www.levreview.com"],
        CANONICAL_HOST="levreview.com",
        SECURE_SSL_REDIRECT=False,
    )
    def test_noncanonical_host_redirects_to_canonical_host(self):
        response = self.client.get("/", secure=True, HTTP_HOST="www.levreview.com")

        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], "https://levreview.com/")
