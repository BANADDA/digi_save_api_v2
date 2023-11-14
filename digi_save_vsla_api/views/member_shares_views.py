from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import MemberShares
from digi_save_vsla_api.serializers import MemberSharesSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def member_shares_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            logged_in_users_id = data.get('logged_in_user_id')
            date = data.get('date')
            share_purchases = data.get('sharePurchases')
            meeting_id = data.get('meetingId')
            users_id = data.get('logged_in_user_id')
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')

            member_shares = MemberShares(
                logged_in_users_id=logged_in_users_id,
                date=date,
                sharePurchases=share_purchases,
                meeting=meeting_id,
                users=users_id,
                group_id=group_id,
                cycle_id=cycle_id,
            )
            member_shares.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Member Shares created successfully',
            })

        if request.method == 'GET':
            # Get all MemberShares objects
            member_shares_list = MemberShares.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each MemberShares object excluding 'id' field
            for member_shares in member_shares_list:
                data = {
                    'logged_in_user_id': member_shares.logged_in_users_id,
                    'date': member_shares.date,
                    'sharePurchases': member_shares.sharePurchases,
                    'meetingId': member_shares.meeting,
                    'group_id': member_shares.group_id,
                    'cycle_id': member_shares.cycle_id,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['memberShares'] = serialized_data.get('memberShares', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)
    
@api_view(['GET', 'PUT', 'DELETE'])
def member_shares_detail(request, pk):
    try:
        member_shares = MemberShares.objects.get(pk=pk)
    except MemberShares.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSharesSerializer(member_shares)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MemberSharesSerializer(member_shares, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member_shares.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)