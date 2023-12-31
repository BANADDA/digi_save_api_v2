# views/assigned_positions_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import AssignedPositions, GroupMembers, GroupProfile, Positions
from digi_save_vsla_api.serializers import AssignedPositionsSerializer

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def assigned_positions_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            id=data.get('id')
            position_name = data.get('position_name')
            members_id = data.get('member_id')
            group_id = data.get('group_id')

            # Get the related instances based on their IDs
            # member = GroupMembers.objects.get(member_id=members_id)
            # group = GroupProfile.objects.get(profile_id=group_id)
            # position = Positions.objects.get(position_id=positions_id)

            assigned_position = AssignedPositions(
                id=id,
                position_id=members_id,
                member_id=position_name,
                group_id=group_id,
            )
            assigned_position.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Assigned position created successfully',
            })

        if request.method == 'GET':
            assigned_positions = AssignedPositions.objects.all()
            assigned_positions_data = {'assigned_positions': []}
            for assigned_position in assigned_positions:
                data = {
                    'id': assigned_position.id,
                    'position_name': assigned_position.position_name,
                    'member_id': assigned_position.member_id,
                    'group_id': assigned_position.group_id,
                }
                assigned_positions_data['assigned_positions'].append(data)
        # Return the serialized data as JSON
        return JsonResponse(assigned_positions_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def assigned_positions_detail(request, pk):
    try:
        assigned_position = AssignedPositions.objects.get(pk=pk)
    except AssignedPositions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssignedPositionsSerializer(assigned_position)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AssignedPositionsSerializer(assigned_position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        assigned_position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

