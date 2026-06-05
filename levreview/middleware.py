from urllib.parse import urlsplit, urlunsplit

from django.conf import settings
from django.shortcuts import redirect


class CanonicalHostRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        canonical_host = getattr(settings, "CANONICAL_HOST", "")
        exempt_hosts = getattr(settings, "CANONICAL_HOST_REDIRECT_EXEMPT_HOSTS", [])
        request_host = request.get_host().split(":")[0]

        if canonical_host and request_host and request_host != canonical_host and request_host not in exempt_hosts:
            parsed_url = urlsplit(request.build_absolute_uri())
            canonical_url = urlunsplit(
                ("https", canonical_host, parsed_url.path, parsed_url.query, parsed_url.fragment)
            )
            return redirect(canonical_url, permanent=True)

        return self.get_response(request)
