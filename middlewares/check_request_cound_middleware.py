from typing import Any

# Django
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse

# Apps
from auths.models import CUser

# Settings
from settings.conf import ADMIN_URL


class CountMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        print("=======================")
        print(type(get_response))

    def __call__(self, request: WSGIRequest, 
                 *args: tuple, **kwds: dict) -> Any:
        print("CUSTOM MIDDLEWARE IS WORK!")
        response = self.get_response(request)
        if ADMIN_URL in request.path:
            return response
        
        if request.user.is_anonymous:
            return HttpResponse('PLZ AUTH PLZ MAN PLZ')
        
        user: CUser = request.user
        user.count_requests -= 1
        if user.count_requests <= 0:
            return HttpResponse("Limit is bound")
        
        user.save()
        return response
