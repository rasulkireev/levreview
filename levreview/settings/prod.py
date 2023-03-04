# prod.py
# Production settings for myapp
from . import *  # Import base settings from settings/__init__.py

ALLOWED_HOSTS = ["www.levreview.com", "levreview.cr.rasulkireev.com"]
DEBUG = False

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
