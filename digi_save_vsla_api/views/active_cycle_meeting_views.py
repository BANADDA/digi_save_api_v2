from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import ActiveCycleMeeting, CycleMeeting, GroupProfile
from digi_save_vsla_api.serializers import ActiveCycleMeetingSerializer

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def active_cycle_meeting_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycle_meeting_id = data.get('cycle_meeting_id')

            active_cycle_meeting = ActiveCycleMeeting(
                group_id=group_id,
                cycleMeetingID=cycle_meeting_id,
            )
            active_cycle_meeting.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Active Cycle Meeting created successfully',
            })

        if request.method == 'GET':
            # Get all ActiveCycleMeeting objects
            active_cycle_meetings = ActiveCycleMeeting.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each ActiveCycleMeeting object excluding 'id' field
            for active_cycle_meeting in active_cycle_meetings:
                data = {
                    'group_id': active_cycle_meeting.group_id,
                    'cycleMeetingID': active_cycle_meeting.cycleMeetingID
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['ActiveCycleMeeting'] = serialized_data.get('ActiveCycleMeeting', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def active_cycle_meeting_detail(request, pk):
    try:
        active_cycle_meeting = ActiveCycleMeeting.objects.get(pk=pk)
    except ActiveCycleMeeting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActiveCycleMeetingSerializer(active_cycle_meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActiveCycleMeetingSerializer(active_cycle_meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        active_cycle_meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
