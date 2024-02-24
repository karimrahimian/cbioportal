from django.contrib.auth import authenticate
from django.http import HttpResponse
from base64 import b64decode


class BasicAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/tissuelist') or request.path.startswith('/api'):
            if 'HTTP_AUTHORIZATION' in request.META:
                auth = request.META['HTTP_AUTHORIZATION'].split()
                if len(auth) == 2 and auth[0].lower() == 'basic':
                    username, password = b64decode(auth[1]).decode('utf-8').split(':')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        request.user = user
                        return self.get_response(request)
                    else:
                        return HttpResponse(status=401)
            else:
                return HttpResponse(status=401)
        else:
            return self.get_response(request)
