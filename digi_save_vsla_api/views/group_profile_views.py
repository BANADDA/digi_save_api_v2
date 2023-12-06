import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import GroupProfile
from digi_save_vsla_api.serializers import GroupProfileSerializer

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def group_profile_list(request):
    data = request.data
    print("Received data:", data.get('groupName'))
    try:
        if request.method == 'POST':
            id=data.get('id'),
            
            print("Received data:", data)
            groupName = data.get('groupName')
            countryOfOrigin = data.get('countryOfOrigin')
            meetingLocation = data.get('meetingLocation')
            groupStatus = data.get('groupStatus')
            groupLogoPath = data.get('groupLogoPath')
            partnerID = data.get('partnerID')
            workingWithPartner = data.get('workingWithPartner')
            isWorkingWithPartner = data.get('isWorkingWithPartner')
            numberOfCycles = data.get('numberOfCycles')
            numberOfMeetings = data.get('numberOfMeetings')
            loanFund = data.get('loanFund')
            socialFund = data.get('socialFund')

            group_profile = GroupProfile(
                id=id,
                groupName=groupName,
                countryOfOrigin=countryOfOrigin,
                meetingLocation=meetingLocation,
                groupStatus=groupStatus,
                groupLogoPath=groupLogoPath,
                partnerID=partnerID,
                workingWithPartner=workingWithPartner,
                isWorkingWithPartner=isWorkingWithPartner,
                numberOfCycles=numberOfCycles,
                numberOfMeetings=numberOfMeetings,
                loanFund=loanFund,
                socialFund=socialFund,
            )
            group_profile.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Group profile created successfully',
            })

        if request.method == 'GET':
            # Get all GroupProfile objects
            group_profiles = GroupProfile.objects.all()

            # Create a dictionary to store the serialized data
            serialized_data = {}

        # Serialize each GroupProfile object excluding 'id' and 'sync_flag'
        for group_profile in group_profiles:
            data = {
                'id': group_profile.id,
                'groupName': group_profile.groupName,
                'countryOfOrigin': group_profile.countryOfOrigin,
                'meetingLocation': group_profile.meetingLocation,
                'groupStatus': group_profile.groupStatus,
                'groupLogoPath': group_profile.groupLogoPath,
                'partnerID': group_profile.partnerID,
                'workingWithPartner': group_profile.workingWithPartner,
                'isWorkingWithPartner': group_profile.isWorkingWithPartner,
                'numberOfCycles': group_profile.numberOfCycles,
                'numberOfMeetings': group_profile.numberOfMeetings,
                'loanFund': group_profile.loanFund,
                'socialFund': group_profile.socialFund,
                # Exclude 'id' and 'sync_flag' fields
            }

            # Add the serialized data to the dictionary using the table name as the key
            serialized_data['group_profile'] = serialized_data.get('group_profile', []) + [data]

        # Return the serialized data as JSON
        return JsonResponse(serialized_data, safe=False)


    # # Handle other HTTP methods if needed
    # return JsonResponse({'error': 'Method Not Allowed'}, status=405)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(('GET', 'PUT', 'DELETE'))
def group_profile_detail(request, pk):
    try:
        group_profile = GroupProfile.objects.get(pk=pk)
    except GroupProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupProfileSerializer(group_profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupProfileSerializer(group_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
