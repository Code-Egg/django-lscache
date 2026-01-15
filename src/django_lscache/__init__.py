from .decorators import lscache
from .middleware import LSCacheMiddleware
from .purging import lscache_purge

default_app_config = "django_lscache.apps.DjangoLSCacheConfig"