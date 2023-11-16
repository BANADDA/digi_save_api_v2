from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from digi_save_vsla_api.auth import PhoneCodeBackend
from digi_save_vsla_api.serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

@csrf_exempt
def login_with_phone_unique_code(request):
    if request.method == 'POST':
        print('Received POST request data:', request.POST)
        serializer = LoginSerializer(data=request.POST)
        
        if serializer.is_valid():
            phone = serializer.validated_data["phone"]
            code = serializer.validated_data["unique_code"]
            backend = PhoneCodeBackend()
            user = backend.authenticate(request=request, phone=phone, unique_code=code)
            print('User object: ', user)
            print('User phone:', phone)
            print('User code:', code)
            
            if user is not None:
                # user = get_user_model().objects.get(id=user.id)
                token, created = Token.objects.get_or_create(user=user)
                if created:
                    token.user = user
                    token.save()
                    print('User token: ',token)

                response_data = {
                    "status": status.HTTP_200_OK,
                    'success': True,
                    "Token": token.key if token else None,
                    'user': {
                        'id': user.id,
                        'fname': user.fname,
                        'lname': user.lname,
                        'email': user.email,
                        'image': user.image,
                        'unique_code':user.unique_code,
                        'phone': user.phone,
                        'sex': user.sex,
                        'country': user.country,
                        'date_of_birth': user.date_of_birth,
                        'district': user.district,
                        'subCounty': user.subCounty,
                        'village': user.village,
                        'number_of_dependents': user.number_of_dependents,
                        'family_information': user.family_information,
                        'next_of_kin_name': user.next_of_kin_name,
                        'next_of_kin_has_phone_number': user.next_of_kin_has_phone_number,
                        'next_of_kin_phone_number': user.next_of_kin_phone_number,
                        'pwd_type': user.pwd_type,
                    },
                }
                return JsonResponse(response_data, status=status.HTTP_200_OK)
            
            else:
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid Email or Password",
                }
                return JsonResponse(response, status=status.HTTP_401_UNAUTHORIZED)
        
        else:
            response = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Bad request",
                "data": serializer.errors
            }
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        response = {
            "status": status.HTTP_405_METHOD_NOT_ALLOWED,
            "message": "Method Not Allowed",
        }
        return JsonResponse(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)