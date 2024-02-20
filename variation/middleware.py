from django.contrib.auth import authenticate


class BasicAuthenticationMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth)==2 and auth[0].lower()=='basic':
                username,password = auth[1].decode('base64').split(':')
                user = authenticate(username=username,password=password)
                if user is not None:
                    request.user = user
        return self.get_response(request)
