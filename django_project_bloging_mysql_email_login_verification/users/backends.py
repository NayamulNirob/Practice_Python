from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import PendingUser
from django.db.models import Q

User = get_user_model()


class PendingUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if PendingUser.objects.filter(Q(username=username) | Q(email=username)).exists():
            return None

            # 2. Try to authenticate using either username or email
        try:
            user = User.objects.get(Q(username=username) | Q(
                email=username))
            if user.check_password(password):
                return user
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            # User.MultipleChoices handles cases where username and email might overlap
            return None

        return None
