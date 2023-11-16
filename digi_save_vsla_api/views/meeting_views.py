from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import Meeting
from digi_save_vsla_api.serializers import MeetingSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def meeting_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
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
            social_fund_contributions = data.get('socialFundContributions')
            share_purchases = data.get('sharePurchases')
            total_loan_fund = data.get('totalLoanFund')
            total_social_fund = data.get('totalSocialFund')
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')

            meeting = Meeting(
                date=date,
                time=time,
                end_time=end_time,
                location=location,
                facilitator=facilitator,
                meetingPurpose=meeting_purpose,
                latitude=latitude,
                longitude=longitude,
                address=address,
                objectives=objectives,
                attendanceData=attendance_data,
                representativeData=representative_data,
                proposals=proposals,
                socialFundContributions=social_fund_contributions,
                sharePurchases=share_purchases,
                totalLoanFund=total_loan_fund,
                totalSocialFund=total_social_fund,
                group_id=group_id,
                cycle_id=cycle_id,
            )
            meeting.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Meeting created successfully',
            })

        if request.method == 'GET':
            # Get all Meeting objects
            meeting_list = Meeting.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each Meeting object excluding 'id' field
            for meeting in meeting_list:
                data = {
                    'date': meeting.date,
                    'time': meeting.time,
                    'endTime': meeting.endTime,
                    'location': meeting.location,
                    'facilitator': meeting.facilitator,
                    'meetingPurpose': meeting.meetingPurpose,
                    'latitude': meeting.latitude,
                    'longitude': meeting.longitude,
                    'address': meeting.address,
                    'objectives': meeting.objectives,
                    'attendanceData': meeting.attendanceData,
                    'representativeData': meeting.representativeData,
                    'proposals': meeting.proposals,
                    'socialFundContributions': meeting.socialFundContributions,
                    'sharePurchases': meeting.sharePurchases,
                    'totalLoanFund': meeting.totalLoanFund,
                    'totalSocialFund': meeting.totalSocialFund,
                    'group_id': meeting.group_id,
                    'cycle_id': meeting.cycle_id,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['meeting'] = serialized_data.get('meeting', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def meeting_detail(request, pk):
    try:
        meeting = Meeting.objects.get(pk=pk)
    except Meeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)