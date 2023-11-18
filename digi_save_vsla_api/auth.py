from django.contrib.auth.backends import BaseBackend as auth_backends
from digi_save_vsla_api.models import Users
class PhoneCodeBackend(auth_backends):
    def authenticate(self, request, phone=None, unique_code=None):
        try:
            user = Users.objects.get(phone=phone, unique_code=unique_code)
            print('Object type:', type(user))
            return user  # Return the User object if found
        except Users.DoesNotExist:
            return None  # If no user found, return None

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
