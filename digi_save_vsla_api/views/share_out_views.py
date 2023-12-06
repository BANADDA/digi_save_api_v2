from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import ShareOut
from digi_save_vsla_api.serializers import ShareOutSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def share_out_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            id=data.get('id'),
            group_id = data.get('group_id')
            cycle_id = data.get('cycleId')
            users_id = data.get('user_id')
            share_value = data.get('share_value')

            share_out = ShareOut(
                id=id,
                group=group_id,
                cycleId=cycle_id,
                users=users_id,
                share_value=share_value,
            )
            share_out.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Share Out created successfully',
            })

        if request.method == 'GET':
            # Get all ShareOut objects
            share_out_list = ShareOut.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each ShareOut object excluding 'id' field
            for share_out in share_out_list:
                data = {
                    'id': share_out.id,
                    'group_id': share_out.group,
                    'cycleId': share_out.cycleId,
                    'user_id': share_out.users,
                    'share_value': share_out.share_value,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['share_out'] = serialized_data.get('share_out', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def share_out_detail(request, pk):
    try:
        share_out = ShareOut.objects.get(pk=pk)
    except ShareOut.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShareOutSerializer(share_out)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShareOutSerializer(share_out, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        share_out.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)