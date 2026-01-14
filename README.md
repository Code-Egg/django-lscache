# django-lscache

A simple **LiteSpeed Cache** integration for Django applications.

## Prerequisite

Running the app on LiteSpeed/OpenLiteSpeed Web Server, and setup the cache folder. 

## Installation
```
pip install django-lscache
```

Add `django_lscache` to your `INSTALLED_APPS` in **settings.py**:
```
INSTALLED_APPS = [
    ...
    'django_lscache',
]
```
Add the middleware:
```
MIDDLEWARE = [
    ...
    'django_lscache.middleware.LSCacheMiddleware',
]
```

## Usage
Use the `@lscache` decorator in your views to cache responses:
```
from django_lscache.decorators import lscache
from django.http import HttpResponse

### No cache header
@lscache()
def index(request):
    return HttpResponse("Hello, world!")

### Returns no-cache
@lscache(max_age=0)
def index(request):
    return HttpResponse("Hello, world!")

### Public cache for 3600 seconds
@lscache(max_age=3600)
def index(request):
    return HttpResponse("Hello, world!")   

### Private cache for 180 seconds
@lscache(max_age=180, cacheability="private")
def contact(request):
    return HttpResponse("Contact page")
```

### Purge ALL command
Purge all cached URLs, run the management command:
```
python manage.py lscache_purge --all
```

Note: The domain used for purging is set in django_lscache/management/commands/lscache_purge.py