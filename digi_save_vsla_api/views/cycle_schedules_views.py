# views/cycle_schedules_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import CycleSchedules, GroupProfile
from digi_save_vsla_api.serializers import CycleSchedulesSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def cycle_schedules_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            
            print("Received data:", data)
            id=data.get('id')
            group_id = data.get('group_id')
            meeting_duration = data.get('meeting_duration')
            number_of_meetings = data.get('number_of_meetings')
            meeting_frequency = data.get('meeting_frequency')
            day_of_week = data.get('day_of_week')
            start_date = data.get('start_date')
            share_out_date = data.get('share_out_date')

            #  # Get the GroupProfile instance based on the group_id
            # group_profile = GroupProfile.objects.get(profile_id=group_id)
            # print('Group profile object: ', group_profile)


            cycle_schedules = CycleSchedules(
                id=id,
                group_id=group_id,
                meeting_duration=meeting_duration,
                number_of_meetings=number_of_meetings,
                meeting_frequency=meeting_frequency,
                day_of_week=day_of_week,
                start_date=start_date,
                share_out_date=share_out_date,
            )
            cycle_schedules.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Cycle Schedle created successfully',
            })

        if request.method == 'GET':
            # Get all CycleSchedules objects
            cycle_schedules = CycleSchedules.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

        # Serialize each CycleSchedules object excluding 'id' and 'sync_flag'
        for cycle_schedules in cycle_schedules:
            data = {
                'id':cycle_schedules.id,
                'group_id': cycle_schedules.group_id,  # assuming you want the group_id's id
                'meeting_duration': cycle_schedules.meeting_duration,
                'number_of_meetings': cycle_schedules.number_of_meetings,
                'meeting_frequency': cycle_schedules.meeting_frequency,
                'day_of_week': cycle_schedules.day_of_week,
                'start_date': cycle_schedules.start_date,
                'share_out_date': cycle_schedules.share_out_date,
                # Exclude 'id' and 'sync_flag' fields
            }
             # Add the serialized data to the dictionary using the table name as the key
            serialized_data['cycle_schedules'] = serialized_data.get('cycle_schedules', []) + [data]

        # Return the serialized data as JSON
        return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def cycle_schedules_detail(request, pk):
    try:
        cycle_schedule = CycleSchedules.objects.get(pk=pk)
    except CycleSchedules.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CycleSchedulesSerializer(cycle_schedule)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CycleSchedulesSerializer(cycle_schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cycle_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
