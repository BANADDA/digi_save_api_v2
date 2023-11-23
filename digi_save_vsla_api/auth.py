from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

class PhoneCodeBackend(BaseBackend):
    def authenticate(self, request, phone=None, unique_code=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(phone=phone)
            if check_password(unique_code, user.unique_code):
                return user
        except User.DoesNotExist:
            return None
