from functools import wraps

def lscache(max_age=None, cacheability="public", esi=False):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)

            if max_age == 0 or cacheability == "no-cache":
                response["X-LiteSpeed-Cache-Control"] = "no-cache"
                return response

            if max_age is None:
                return response

            header = f"max-age={int(max_age)},{cacheability}"
            if esi:
                header += ",esi=on"

            response["X-LiteSpeed-Cache-Control"] = header
            return response

        return wrapper
    return decorator
