from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import Social
from digi_save_vsla_api.serializers import SocialSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def social_list(request):
    data = request.data
    print("Received data:", data.get('meetingId'))
    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            social_fund = data.get('socialFund')
            meeting_id = data.get('meetingId')

            social = Social(
                group_id=group_id,
                socialFund=social_fund,
                meetingId=meeting_id,
            )
            social.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Social created successfully',
            })

        if request.method == 'GET':
            # Get all Social objects
            social_list = Social.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each Social object excluding 'id' field
            for social in social_list:
                data = {
                    'group_id':social.group_id,
                    'socialFund': social.socialFund,
                    'meetingId': social.meetingId,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['social'] = serialized_data.get('social', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def social_detail(request, pk):
    try:
        social = Social.objects.get(pk=pk)
    except Social.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialSerializer(social)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialSerializer(social, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        social.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)