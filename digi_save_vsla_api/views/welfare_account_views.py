from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import WelfareAccount
from digi_save_vsla_api.serializers import WelfareAccountSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def welfare_account_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            logged_in_users_id = data.get('logged_in_user_id')
            amount = data.get('amount')
            group_id = data.get('group_id')
            meeting_id = data.get('meeting_id')
            cycle_id = data.get('cycle_id')
            
            welfare_account = WelfareAccount(
                logged_in_users_id=logged_in_users_id,
                amount=amount,
                group_id=group_id,
                meeting_id=meeting_id,
                cycle_id=cycle_id,
            )
            welfare_account.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Welfare Account created successfully',
            })

        if request.method == 'GET':
            # Get all WelfareAccount objects
            welfare_account_list = WelfareAccount.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each WelfareAccount object excluding 'id' field
            for welfare_account in welfare_account_list:
                data = {
                    'logged_in_user_id': welfare_account.logged_in_users_id,
                    'amount': welfare_account.amount,
                    'group_id': welfare_account.group_id,
                    'meeting_id': welfare_account.meeting_id,
                    'cycle_id': welfare_account.cycle_id,
                    'sync_flag': welfare_account.sync_flag,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['welfare_account'] = serialized_data.get('welfare_account', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def welfare_account_detail(request, pk):
    try:
        welfare_account = WelfareAccount.objects.get(pk=pk)
    except WelfareAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WelfareAccountSerializer(welfare_account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WelfareAccountSerializer(welfare_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        welfare_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)