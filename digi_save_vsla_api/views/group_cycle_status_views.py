from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import CycleMeeting, GroupCycleStatus, GroupProfile
from digi_save_vsla_api.serializers import GroupCycleStatusSerializer

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def group_cycle_status_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            id=data.get('id'),
            group = data.get('group_id')
            cycle_id = data.get('cycleId')
            is_cycle_started = data.get('is_cycle_started')

            group_cycle_status = GroupCycleStatus(
                id=id,
                group=group,
                cycleId=cycle_id,
                is_cycle_started=is_cycle_started,
            )
            group_cycle_status.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Group Cycle Status created successfully',
            })

        if request.method == 'GET':
            # Get all GroupCycleStatus objects
            group_cycle_status_list = GroupCycleStatus.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each GroupCycleStatus object excluding 'id' field
            for group_cycle_status in group_cycle_status_list:
                data = {
                    'id': group_cycle_status.id,
                    'group_id': group_cycle_status.group,
                    'cycleId': group_cycle_status.cycleId,
                    'is_cycle_started': group_cycle_status.is_cycle_started,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['group_cycle_status'] = serialized_data.get('group_cycle_status', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)
    
def group_cycle_status_detail(request, pk):
    try:
        group_cycle_status = GroupCycleStatus.objects.get(pk=pk)
    except GroupCycleStatus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupCycleStatusSerializer(group_cycle_status)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupCycleStatusSerializer(group_cycle_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_cycle_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)