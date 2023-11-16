from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed

from digi_save_vsla_api.models import Users

class PhoneCodeBackend:
    def authenticate(self, request, phone=None, unique_code=None):
        try:
            user = Users.objects.get(phone=phone, unique_code=unique_code)
        except Users.DoesNotExist:
            raise AuthenticationFailed('User not found')

        return user

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
