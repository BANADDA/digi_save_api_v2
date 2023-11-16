from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import Shares
from digi_save_vsla_api.serializers import SharesSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def shares_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            share_purchases = data.get('sharePurchases')
            meeting_id = data.get('meetingId')
            cycle_id = data.get('cycle_id')
            group_id = data.get('group_id')

            shares = Shares(
                sharePurchases=share_purchases,
                meetingId=meeting_id,
                cycle_id=cycle_id,
                group_id=group_id,
            )
            shares.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Shares created successfully',
            })

        if request.method == 'GET':
            # Get all Shares objects
            shares_list = Shares.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each Shares object excluding 'id' field
            for shares in shares_list:
                data = {
                    'sharePurchases': shares.sharePurchases,
                    'meetingId': shares.meetingId,
                    'cycle_id': shares.cycle_id,
                    'group_id': shares.group_id,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['shares'] = serialized_data.get('shares', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def shares_detail(request, pk):
    try:
        shares = Shares.objects.get(pk=pk)
    except Shares.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SharesSerializer(shares)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SharesSerializer(shares, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        shares.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)