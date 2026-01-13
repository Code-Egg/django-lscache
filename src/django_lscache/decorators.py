from functools import wraps
from django.http import HttpResponse

def lscache(max_age=60):
    """
    Decorator for Django views to add LiteSpeed Cache headers.

    Args:
        max_age (int): Cache duration in seconds.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)
            if isinstance(response, HttpResponse):
                response["X-LiteSpeed-Cache"] = "hit,private"
                response["Cache-Control"] = f"max-age={max_age}, public"
            return response
        return wrapper
    return decorator
