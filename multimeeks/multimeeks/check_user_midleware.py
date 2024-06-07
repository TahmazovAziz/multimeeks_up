from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from django.urls import reverse
from django.http import HttpResponseForbidden
from cinema.models import Media
class CheckUserMidleware:
    
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = reverse('administration')
        if request.path == url:
            if not request.user.is_superuser:
                return HttpResponseForbidden()
        return self.get_response(request)