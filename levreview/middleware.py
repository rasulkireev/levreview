from django.conf import settings
from django.shortcuts import redirect


class CanonicalHostRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        canonical_host = getattr(settings, "CANONICAL_HOST", "")
        request_host = request.get_host().split(":")[0]

        if canonical_host and request_host and request_host != canonical_host:
            url = request.build_absolute_uri()
            canonical_url = url.replace(request.get_host(), canonical_host, 1)
            return redirect(canonical_url, permanent=True)

        return self.get_response(request)
