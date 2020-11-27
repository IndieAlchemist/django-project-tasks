from django.http import HttpResponse
from django.conf import settings

class BlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        if ip in settings.BLACKLIST:
            print(f'IP: {ip} in blacklist - not allowed')
            return HttpResponse(status=403)


        response = self.get_response(request)
        return response
