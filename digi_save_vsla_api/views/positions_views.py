# views/positions_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import Positions
from digi_save_vsla_api.serializers import PositionsSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def positions_list(request):
    data = request.data
    print("Received data:", data)
    try:
        if request.method == 'POST':
            id=data.get('id'),
            
            print("Received data:", data)
            name = data.get('name')

            group_members = Positions(
                id=id,
                name=name,
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
            serialized_data = []

        # Serialize each Positions object excluding 'id' and 'sync_flag'
        for position in positions:
            print('Positions:', position)
            try:
                serialized_data.append({
            'id': position.id,
              'name': position.name
              })
            except Exception as e:
                return JsonResponse({
            'status': 'error',
            'message': str(e),
            }, status=500) 
        return JsonResponse({
                  'status': 'success',
                  'positions': serialized_data,
                  })
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
