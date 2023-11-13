# views/positions_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Positions
from digi_save_vsla_api.serializers import PositionsSerializer

@api_view(['GET', 'POST'])
def positions_list(request):
    data = request.data
    print("Received data:", data)
    try:
        if request.method == 'POST':
            
            print("Received data:", data)
            name = data.get('name')
            position_id = data.get('id')
            sync_flag = data.get('sync_flag')

            group_members = Positions(
                name=name,
                position_id=position_id,
                sync_flag=sync_flag,
            )
            group_members.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Positions created successfully',
            })

        if request.method == 'GET':
            # Get all Positions objects
            positions = Positions.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

        # Serialize each Positions object excluding 'id' and 'sync_flag'
        for position in positions:
            data = {
                'name': position.name,
                # Exclude 'id' and 'sync_flag' fields
            }

            # Add the serialized data to the dictionary using the table name as the key
            serialized_data['positions'] = serialized_data.get('positions', []) + [data]

        # Return the serialized data as JSON
        return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def positions_detail(request, pk):
    try:
        position = Positions.objects.get(pk=pk)
    except Positions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PositionsSerializer(position)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PositionsSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
