from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import *
from digi_save_vsla_api.serializers import LoanPaymentsSerializer

@api_view(['GET', 'POST'])
def loan_payments_list(request):
    data = request.data
    print("Received data:", data.get('groupId'))
    try:
        if request.method == 'POST':
            member = data.get('member_id')
            group = data.get('groupId')
            loan = data.get('loan_id')
            payment_amount = data.get('payment_amount')
            payment_date = data.get('payment_date')

            loan_payment = LoanPayments(
                member=member,
                group=group,
                loan=loan,
                payment_amount=payment_amount,
                payment_date=payment_date,
            )
            loan_payment.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Loan Payment created successfully',
            })

        if request.method == 'GET':
            # Get all LoanPayments objects
            loan_payments_list = LoanPayments.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each LoanPayments object excluding 'id' field
            for loan_payment in loan_payments_list:
                data = {
                    'member_id': loan_payment.member,
                    'groupId': loan_payment.group,
                    'loan_id': loan_payment.loan,
                    'payment_amount': loan_payment.payment_amount,
                    'payment_date': loan_payment.payment_date,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['loan_payments'] = serialized_data.get('loan_payments', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def loan_payments_detail(request, pk):
    try:
        loan_payment = LoanPayments.objects.get(pk=pk)
    except LoanPayments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanPaymentsSerializer(loan_payment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanPaymentsSerializer(loan_payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan_payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)