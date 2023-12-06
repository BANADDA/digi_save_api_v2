from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import CycleMeeting, GroupForm, GroupProfile
from digi_save_vsla_api.serializers import CycleMeetingSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cycle_meeting_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            id=data.get('id')
            date = data.get('date')
            time = data.get('time')
            end_time = data.get('endTime')
            location = data.get('location')
            facilitator = data.get('facilitator')
            meeting_purpose = data.get('meetingPurpose')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            address = data.get('address')
            objectives = data.get('objectives')
            attendance_data = data.get('attendanceData')
            representative_data = data.get('representativeData')
            proposals = data.get('proposals')
            total_loan_fund = data.get('totalLoanFund')
            total_social_fund = data.get('totalSocialFund')
            social_fund_contributions = data.get('socialFundContributions')
            share_purchases = data.get('sharePurchases')
            group_id = data.get('group_id')

            cycle_meeting = CycleMeeting(
                id=id,
                date=date,
                time=time,
                endTime=end_time,
                location=location,
                facilitator=facilitator,
                meetingPurpose=meeting_purpose,
                latitude=latitude,
                longitude=longitude,
                address=address,
                objectives=objectives,
                attendanceData=attendance_data,
                representative_data=representative_data,
                proposals=proposals,
                totalLoanFund=total_loan_fund,
                totalSocialFund=total_social_fund,
                socialFundContributions=social_fund_contributions,
                sharePurchases=share_purchases,
                group_id=group_id,
            )
            cycle_meeting.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Cycle Meeting created successfully',
            })

        if request.method == 'GET':
            # Get all CycleMeeting objects
            cycle_meeting_list = CycleMeeting.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each CycleMeeting object excluding 'id' field
            for cycle_meeting in cycle_meeting_list:
                data = {
                    'id': cycle_meeting.id,
                    'date': cycle_meeting.date,
                    'time': cycle_meeting.time,
                    'endTime': cycle_meeting.endTime,
                    'location': cycle_meeting.location,
                    'facilitator': cycle_meeting.facilitator,
                    'meetingPurpose': cycle_meeting.meetingPurpose,
                    'latitude': cycle_meeting.latitude,
                    'longitude': cycle_meeting.longitude,
                    'address': cycle_meeting.address,
                    'objectives': cycle_meeting.objectives,
                    'attendanceData': cycle_meeting.attendanceData,
                    'representativeData': cycle_meeting.representativeData,
                    'proposals': cycle_meeting.proposals,
                    'totalLoanFund': cycle_meeting.totalLoanFund,
                    'totalSocialFund': cycle_meeting.totalSocialFund,
                    'socialFundContributions': cycle_meeting.socialFundContributions,
                    'sharePurchases': cycle_meeting.sharePurchases,
                    'group_id': cycle_meeting.group_id,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['cyclemeeting'] = serialized_data.get('cyclemeeting', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def cycle_meeting_detail(request, pk):
    try:
        cycle_meeting = CycleMeeting.objects.get(pk=pk)
    except CycleMeeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleMeetingSerializer(cycle_meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CycleMeetingSerializer(cycle_meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cycle_meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)