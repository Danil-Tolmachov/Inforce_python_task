from django.core.handlers.wsgi import WSGIRequest
from django.core.exceptions import ImproperlyConfigured
from menu_api.settings import API_VERSIONS


class VersionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        version = request.headers.get('Access-Version')

        if API_VERSIONS is None:
            raise ImproperlyConfigured('Set API_VERSIONS variable')

        for api_version, urlpatterns in API_VERSIONS.items():
            if version == api_version:
                request = WSGIRequest(request.environ)
                request.urlconf = urlpatterns
                break
        
        response = self.get_response(request)
        return response