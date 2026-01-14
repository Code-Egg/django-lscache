from django.utils.deprecation import MiddlewareMixin

class LSCacheMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        return response
