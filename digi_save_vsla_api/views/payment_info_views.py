from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import PaymentInfo
from digi_save_vsla_api.serializers import PaymentInfoSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def payment_info_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
            meeting_id = data.get('meeting_id')
            member_id = data.get('member_id')
            payment_amount = data.get('payment_amount')
            payment_date = data.get('payment_date')
            sync_flag = data.get('sync_flag')

            payment_info = PaymentInfo(
                group=group_id,
                cycle_id=cycle_id,
                meeting_id=meeting_id,
                payment_amount=payment_amount,
                member_id=member_id,
                payment_date=payment_date,
                sync_flag=sync_flag,
            )
            payment_info.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Payment Info created successfully',
            })

        if request.method == 'GET':
            # Get all PaymentInfo objects
            payment_info_list = PaymentInfo.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each PaymentInfo object excluding 'id' field
            for payment_info in payment_info_list:
                data = {
                    'group_id': payment_info.group,
                    'cycle_id': payment_info.cycle_id,
                    'meeting_id': payment_info.meeting_id,
                    'payment_amount': payment_info.payment_amount,
                    'member_id':payment_info.meeting_id,
                    'payment_date': payment_info.payment_date,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['payment_info'] = serialized_data.get('payment_info', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def payment_info_detail(request, pk):
    try:
        payment_info = PaymentInfo.objects.get(pk=pk)
    except PaymentInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentInfoSerializer(payment_info)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PaymentInfoSerializer(payment_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        payment_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)