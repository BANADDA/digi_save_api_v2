from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from digi_save_vsla_api.models import *
from rest_framework.authtoken.models import Token
from digi_save_vsla_api.serializers import UserProfilesSerializer, UsersSerializer

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def user_profiles_list(request):
    if request.method == 'POST':
        data = request.data
        try:
            UserProfiles.objects.create(
                id=data.get('id'),
                unique_code=data.get('unique_code'),
                fname=data.get('fname'),
                lname=data.get('lname'),
                phone=data.get('phone'),
                sex=data.get('sex'),
                date_of_birth=data.get('date_of_birth'),
                image=data.get('image'),
                country=data.get('country'),
                district=District.objects.get(id=data.get('district')),
                subCounty=Subcounty.objects.get(id=data.get('subCounty')),
                village=Village.objects.get(id=data.get('village')),
                number_of_dependents=data.get('number_of_dependents'),
                family_information=data.get('family_information'),
                next_of_kin_name=data.get('next_of_kin_name'),
                next_of_kin_has_phone_number=data.get('next_of_kin_has_phone_number'),
                next_of_kin_phone_number=data.get('next_of_kin_phone_number'),
                pwd_type=data.get('pwd_type')
            )
            return JsonResponse({
                'status': 'success',
                'message': 'User Profile Created successfully',
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e),
            }, status=500)

    elif request.method == 'GET':
        profiles = UserProfiles.objects.all()
        user_data = []
        for profile in profiles:
            print('Profile:', profile)
            try:
                user_data.append({
                'id': profile.id,
                'unique_code': profile.unique_code,
                'fname': profile.fname,
                'lname': profile.lname,
                'email': profile.email,
                'phone': profile.phone,
                'sex': profile.sex,
                'date_of_birth': profile.date_of_birth,
                'image': profile.image,
                'country': profile.country if profile.country else None,
                'district': profile.district.name if profile.district else None,
                'subCounty': profile.subCounty.name if profile.subCounty else None,
                'village': profile.village.name if profile.village else None,
                'number_of_dependents': profile.number_of_dependents,
                'family_information': profile.family_information,
                'next_of_kin_name': profile.next_of_kin_name,
                'next_of_kin_has_phone_number': profile.next_of_kin_has_phone_number,
                'next_of_kin_phone_number': profile.next_of_kin_phone_number,
                'pwd_type': profile.pwd_type,
               })
            except Exception as e:
                return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500) 
    return JsonResponse({
                  'status': 'success',
                  'users': user_data,
                  })

            
                
                
@api_view(['POST'])
@permission_classes([AllowAny])
def generate_users_logins(request):
    data = request.data
    try:
        # general responses
        status = "Failed"
        message = "Invalid phone number"

        # get userprofile object 
        profile = UserProfiles.objects.get(phone=data.get('phone'))

        if profile and not profile.user_id:
            # Check if a User with the same phone number already exists
            existing_user = Users.objects.filter(phone=profile.phone).first()

            if not existing_user:
                # If a User doesn't exist, create one
                new_user = Users.objects.create(
                    unique_code=profile.unique_code,
                    fname=profile.fname,
                    lname=profile.lname,
                    email=profile.email,
                    phone=profile.phone,
                    sex=profile.sex,
                ).save()
                profile.user_id = new_user
                profile.save()
                status = "Success"
                message = "User created successfully"
            else:
                status = "Success"
                message = "User already exists"

            # Return a response
            return JsonResponse({"status": status, "message": message})

        else:
            return JsonResponse({"status": status, "message": message})

    except UserProfiles.DoesNotExist:
        return JsonResponse({"status": status, "message": "UserProfile not found"}) 

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def users_list(request):
    if request.method == 'POST':
        data = request.data
        try:
            # user = Users(
            #     unique_code=data.get('unique_code'),
            #     fname=data.get('fname'),
            #     lname=data.get('lname'),
            #     email=data.get('email'),
            #     phone=data.get('phone'),
            #     sex=data.get('sex'),
            # ).save()
            
            # print(user)
            
            UserProfiles.objects.create(
                # user_id=user.id,
                date_of_birth=data.get('date_of_birth'),
                image=data.get('image'),
                country = data.get('country'),
                district=District.objects.get(id=data.get('district')),
                subCounty=Subcounty.objects.get(id=data.get('subCounty')),
                village=Village.objects.get(id=data.get('village')),
                number_of_dependents = data.get('number_of_dependents'),
                family_information = data.get('family_information'),
                next_of_kin_name = data.get('next_of_kin_name'),
                next_of_kin_has_phone_number = data.get('next_of_kin_has_phone_number'),
                next_of_kin_phone_number = data.get('next_of_kin_phone_number'),
                pwd_type = data.get('pwd_type')
            )

            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.user = user
                token.save()

            return JsonResponse({
                'status': 'success',
                'message': 'User created successfully',
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e),
            }, status=500)

    elif request.method == 'GET':
        users = Users.objects.all()
        user_data = []
        for user in users:
            profile = UserProfiles.objects.get(user_id=user.id)
            user_data.append({
                'id': user.id,
                'unique_code': user.unique_code,
                'fname': user.fname,
                'lname': user.lname,
                'email': user.email,
                'phone': user.phone,
                'sex': user.sex,
                'date_of_birth': profile.date_of_birth,
                'image': profile.image,
                'country': profile.country.name if profile.country else None,
                'district': profile.district.name if profile.district else None,
                'subCounty': profile.subCounty.name if profile.subCounty else None,
                'village': profile.village.name if profile.village else None,
                'number_of_dependents': profile.number_of_dependents,
                'family_information': profile.family_information,
                'next_of_kin_name': profile.next_of_kin_name,
                'next_of_kin_has_phone_number': profile.next_of_kin_has_phone_number,
                'next_of_kin_phone_number': profile.next_of_kin_phone_number,
                'pwd_type': profile.pwd_type,
            })

        return JsonResponse({
            'status': 'success',
            'users': user_data,
        })

@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
        profile = UserProfiles.objects.get(user_id=user)
    except Users.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except UserProfiles.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User profile does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_data = {
            'id': user.id,
            'unique_code': user.unique_code,
            'fname': user.fname,
            'lname': user.lname,
            'email': user.email,
            'phone': user.phone,
            'sex': user.sex,
            'date_of_birth': profile.date_of_birth,
            'image': profile.image,
            # Include other fields from UserProfiles
        }
        return JsonResponse({'status': 'success', 'user': user_data})

    elif request.method == 'PUT':
        user_data = request.data.get('user', {})
        profile_data = request.data.get('profile', {})

        user_serializer = UsersSerializer(user, data=user_data, partial=True)
        profile_serializer = UserProfilesSerializer(profile, data=profile_data, partial=True)

        if user_serializer.is_valid() and profile_serializer.is_valid():
            user_serializer.save()
            profile_serializer.save()
            return JsonResponse({'status': 'success', 'message': 'User updated successfully'})
        return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        profile.delete()
        return JsonResponse({'status': 'success', 'message': 'User deleted successfully'})
