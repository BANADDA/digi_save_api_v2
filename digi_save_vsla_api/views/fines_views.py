from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleMeeting, Fines, GroupForm, GroupMembers, Meeting, SavingsAccount
from digi_save_vsla_api.serializers import FinesSerializer

@api_view(['GET', 'POST'])
def fines_list(request):
    data = request.data
    print("Received data:", data.get('memberId'))
    try:
        if request.method == 'POST':
            member_id = data.get('memberId')
            amount = data.get('amount')
            reason = data.get('reason')
            group_id = data.get('groupId')
            cycle_id = data.get('cycleId')
            meeting_id = data.get('meetingId')
            savings_account_id = data.get('savingsAccountId')
            sync_flag = data.get('sync_flag')

            fines = Fines(
                memberId=member_id,
                amount=amount,
                reason=reason,
                groupId=group_id,
                cycleId=cycle_id,
                meetingId=meeting_id,
                savingsAccountId=savings_account_id,
                sync_flag=sync_flag,
            )
            fines.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Fine created successfully',
            })

        if request.method == 'GET':
            # Get all Fines objects
            fines_list = Fines.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each Fines object excluding 'id' field
            for fines in fines_list:
                data = {
                    'memberId': fines.memberId,
                    'amount': fines.amount,
                    'reason': fines.reason,
                    'groupId': fines.groupId,
                    'cycleId': fines.cycleId,
                    'meetingId': fines.meetingId,
                    'savingsAccountId': fines.savingsAccountId,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['fines'] = serialized_data.get('fines', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def fines_detail(request, pk):
    try:
        fines = Fines.objects.get(pk=pk)
    except Fines.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FinesSerializer(fines)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FinesSerializer(fines, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)