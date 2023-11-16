# views/savings_account_views.py
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import SavingsAccount
from digi_save_vsla_api.serializers import SavingsAccountSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def savings_account_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            logged_in_users_id = data.get('logged_in_user_id')
            date = data.get('date')
            purpose = data.get('purpose')
            amount = data.get('amount')
            group_id = data.get('group_id')

            savings_account = SavingsAccount(
                logged_in_users_id=logged_in_users_id,
                date=date,
                purpose=purpose,
                amount=amount,
                group=group_id,
            )
            savings_account.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Savings Account created successfully',
            })

        if request.method == 'GET':
            # Get all SavingsAccount objects
            savings_account_list = SavingsAccount.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each SavingsAccount object excluding 'id' field
            for savings_account in savings_account_list:
                data = {
                    'logged_in_user_id': savings_account.logged_in_users_id,
                    'date': savings_account.date,
                    'purpose': savings_account.purpose,
                    'amount': savings_account.amount,
                    'group_id': savings_account.group,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['savings_account'] = serialized_data.get('savings_account', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def savings_account_detail(request, pk):
    try:
        savings_account = SavingsAccount.objects.get(pk=pk)
    except SavingsAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SavingsAccountSerializer(savings_account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SavingsAccountSerializer(savings_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        savings_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
