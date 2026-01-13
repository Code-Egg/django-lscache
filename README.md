# django-lscache

This is a sample LiteSpeed Cache plugin for Django applications.

##

pip install --force-reinstall git+https://github.com/Code-Egg/django-lscache.git


INSTALLED_APPS = [
    ...
    "django_lscache",
]

MIDDLEWARE = [
    ...
    "django_lscache.middleware.LSCacheMiddleware",
]


##
Use decorator in views:
```
from django_lscache.decorators import lscache
from django.http import HttpResponse

@lscache(max_age=30)
def index(request):
    return HttpResponse("Hello, world!")
```
