from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from digi_save_vsla_api.auth import PhoneCodeBackend
from digi_save_vsla_api.models import UserProfiles
from digi_save_vsla_api.serializers import LoginSerializer
from rest_framework.authtoken.models import Token

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
                try:
                  token, created = Token.objects.get_or_create(user=user)
                  print('User: ',user)
                  print('User token: ',token)
                  if created:
                        token.user = user
                        token.save()
                        print('User token: ',token)
                except Exception as e:
                   return JsonResponse({
                    'status': 'error in token',
                    'message': str(e),
                }, status=500)
                   
                user_profile = UserProfiles.objects.get(user_id=user)
                
                response_data = {
                "status": status.HTTP_200_OK,
                'success': True,
                "Token": token.key if token else None,
                "is_admin": True,
                'user': {
                    'id': user_profile.id,
                    'fname': user.fname,
                    'lname': user.lname,
                    'email': user.email,
                    'unique_code':user.unique_code,
                    'phone': user.phone,
                    'sex': user.sex,
                    # Include UserProfiles data here
                    'date_of_birth': user_profile.date_of_birth,
                    'image': user_profile.image,
                    'country': user_profile.country if user_profile.country else None,
                    'district': user_profile.district.name if user_profile.district else None,
                    'subCounty': user_profile.subCounty.name if user_profile.subCounty else None,
                    'village': user_profile.village.name if user_profile.village else None,
                    'number_of_dependents': user_profile.number_of_dependents,
                    'family_information': user_profile.family_information,
                    'next_of_kin_name': user_profile.next_of_kin_name,
                    'next_of_kin_has_phone_number': user_profile.next_of_kin_has_phone_number,
                    'next_of_kin_phone_number': user_profile.next_of_kin_phone_number,
                    'pwd_type': user_profile.pwd_type,
                },
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)
            
        else:
            return JsonResponse({'status': 'Authentication failed'}, status=401)
    else:
        response = {
            "status": status.HTTP_405_METHOD_NOT_ALLOWED,
            "message": "Method Not Allowed",
        }
        return JsonResponse(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)