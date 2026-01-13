from .decorators import lscache
from .middleware import LSCacheMiddleware
from .purging import purge_all

default_app_config = "django_lscache.apps.DjangoLSCacheConfig"