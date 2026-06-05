# prod.py
# Production settings for myapp
from . import *  # Import base settings from settings/__init__.py

ALLOWED_HOSTS = ["levreview.com", "www.levreview.com", "levreview.cr.lvtd.dev"]
CSRF_TRUSTED_ORIGINS = ["https://levreview.com", "https://www.levreview.com", "https://levreview.cr.lvtd.dev"]

DEBUG = False
CANONICAL_HOST = "levreview.com"
CANONICAL_HOST_REDIRECT_EXEMPT_HOSTS = ["levreview.cr.lvtd.dev"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "app.log",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {"handlers": ["file"], "level": "INFO", "propagate": True},
    },
    "formatters": {
        "app": {
            "format": ("%(asctime)s [%(levelname)-8s] " "(%(module)s.%(funcName)s) %(message)s"),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}
