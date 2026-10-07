from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import PendingUser
from django.core.exceptions import PermissionDenied


User = get_user_model()

class PendingUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if PendingUser.objects.filter(username=username).exists():
            return None
      
        return super().authenticate(request,username=username, password=password,**kwargs)