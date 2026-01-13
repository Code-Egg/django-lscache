from django.conf import settings
import warnings

def ensure_middleware():
    mw = "django_lscache.middleware.LSCacheMiddleware"
    if mw not in settings.MIDDLEWARE:
        warnings.warn(f"{mw} is not in MIDDLEWARE. Add it manually.")
