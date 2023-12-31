from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import GroupFees, GroupForm, GroupMembers
from digi_save_vsla_api.serializers import GroupFeesSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def group_fees_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            id=data.get('id'),
            member_id = data.get('member_id')
            group_id = data.get('group_id')
            registration_fee = data.get('registration_fee')

            # Get the related instances based on their IDs
            # member = GroupMembers.objects.get(member_id=members_id)
            # group = GroupForm.objects.get(id=group_id)

            fee = GroupFees(
                id=id,
                member=member_id,
                group_id=group_id,
                registration_fee=registration_fee,
            )
            fee.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Fee created successfully',
            })

        if request.method == 'GET':
            # Get all GroupFees objects
            group_fees = GroupFees.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

        # Serialize each GroupFees object excluding 'id' and 'sync_flag'
        for group_fees in group_fees:
            data = {
                'id': group_fees.id,
                'member_id': group_fees.member,  # assuming you want the member's id
                'group_id': group_fees.group_id,  # assuming you want the group_id's id
                'registration_fee': group_fees.registration_fee,
                # Exclude 'id' and 'sync_flag' fields
            }
             # Add the serialized data to the dictionary using the table name as the key
            serialized_data['group_fees'] = serialized_data.get('group_fees', []) + [data]

        # Return the serialized data as JSON
        return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def group_fees_detail(request, pk):
    try:
        group_fees = GroupFees.objects.get(pk=pk)
    except GroupFees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupFeesSerializer(group_fees)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupFeesSerializer(group_fees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_fees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)