from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleStartMeeting
from digi_save_vsla_api.serializers import CycleStartMeetingSerializer

@api_view(['GET', 'POST'])
def cycle_start_meeting_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            group  = data.get('group_id')
            date = data.get('date')
            time = data.get('time')
            location = data.get('location')
            facilitator = data.get('facilitator')
            meeting_purpose = data.get('meeting_purpose')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            address = data.get('address')
            objectives = data.get('objectives')
            attendance_data = data.get('attendance_data')
            representative_data = data.get('representative_data')
            proposals = data.get('proposals')
            end_time = data.get('end_time')
            assigned_funds = data.get('assigned_funds')
            social_fund_bag = data.get('social_fund_bag')
            social_fund_contributions = data.get('social_fund_contributions')
            share_purchases = data.get('share_purchases')
            sync_flag = data.get('sync_flag')

            cycle_start_meeting = CycleStartMeeting(
                group=group,
                date=date,
                time=time,
                location=location,
                facilitator=facilitator,
                meeting_purpose=meeting_purpose,
                latitude=latitude,
                longitude=longitude,
                address=address,
                objectives=objectives,
                attendance_data=attendance_data,
                representative_data=representative_data,
                proposals=proposals,
                end_time=end_time,
                assigned_funds=assigned_funds,
                social_fund_bag=social_fund_bag,
                social_fund_contributions=social_fund_contributions,
                share_purchases=share_purchases,
                sync_flag=sync_flag,
            )
            cycle_start_meeting.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Cycle Start Meeting created successfully',
            })

        if request.method == 'GET':
            # Get all CycleStartMeeting objects
            cycle_start_meetings = CycleStartMeeting.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each CycleStartMeeting object excluding 'id' field
            for cycle_start_meeting in cycle_start_meetings:
                data = {
                    'group_id':cycle_start_meeting.group,
                    'date': cycle_start_meeting.date,
                    'time': cycle_start_meeting.time,
                    'location': cycle_start_meeting.location,
                    'facilitator': cycle_start_meeting.facilitator,
                    'meeting_purpose': cycle_start_meeting.meeting_purpose,
                    'latitude': cycle_start_meeting.latitude,
                    'longitude': cycle_start_meeting.longitude,
                    'address': cycle_start_meeting.address,
                    'objectives': cycle_start_meeting.objectives,
                    'attendance_data': cycle_start_meeting.attendance_data,
                    'representative_data': cycle_start_meeting.representative_data,
                    'proposals': cycle_start_meeting.proposals,
                    'end_time': cycle_start_meeting.end_time,
                    'assigned_funds': cycle_start_meeting.assigned_funds,
                    'social_fund_bag': cycle_start_meeting.social_fund_bag,
                    'social_fund_contributions': cycle_start_meeting.social_fund_contributions,
                    'share_purchases': cycle_start_meeting.share_purchases,
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
def cycle_start_meeting_detail(request, pk):
    try:
        cycle_start_meeting = CycleStartMeeting.objects.get(pk=pk)
    except CycleStartMeeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleStartMeetingSerializer(cycle_start_meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CycleStartMeetingSerializer(cycle_start_meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cycle_start_meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)