from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

# Updated auth backend
class PhoneCodeBackend(BaseBackend):
    def authenticate(self, request, phone=None, unique_code=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(phone=phone)
            print(f"User found with phone number: {user.phone}")
            
            stored_hashed_password = user.unique_code
            print(f"Stored Hashed Password: {stored_hashed_password}")  # Debug line
            
            if check_password(unique_code, stored_hashed_password):
                print("Password matched")
                return user
            else:
                print("Password did not match")
        except User.DoesNotExist:
            print("User does not exist")
            return None
