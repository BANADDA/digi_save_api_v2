from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import CycleMeeting, GroupForm, GroupMembers, LoanDisbursement, Loans
from digi_save_vsla_api.serializers import LoanDisbursementSerializer

@api_view(['GET', 'POST'])
def loan_disbursement_list(request):
    data = request.data
    print("Received data:", data.get('groupId'))
    try:
        if request.method == 'POST':
            member = data.get('member_id')
            group = data.get('groupId')
            cycle_id = data.get('cycleId')
            loan = data.get('loan_id')
            disbursement_amount = data.get('disbursement_amount')
            disbursement_date = data.get('disbursement_date')

            loan_disbursement = LoanDisbursement(
                member=member,
                group=group,
                cycleId=cycle_id,
                loan=loan,
                disbursement_amount=disbursement_amount,
                disbursement_date=disbursement_date,
            )
            loan_disbursement.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Loan Disbursement created successfully',
            })

        if request.method == 'GET':
            # Get all LoanDisbursement objects
            loan_disbursement_list = LoanDisbursement.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each LoanDisbursement object excluding 'id' field
            for loan_disbursement in loan_disbursement_list:
                data = {
                    'member_id': loan_disbursement.member,
                    'groupId': loan_disbursement.group,
                    'cycleId': loan_disbursement.cycleId,
                    'loan_id': loan_disbursement.loan,
                    'disbursement_amount': loan_disbursement.disbursement_amount,
                    'disbursement_date': loan_disbursement.disbursement_date,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['loan_disbursement'] = serialized_data.get('loan_disbursement', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def loan_disbursement_detail(request, pk):
    try:
        loan_disbursement = LoanDisbursement.objects.get(pk=pk)
    except LoanDisbursement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanDisbursementSerializer(loan_disbursement)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanDisbursementSerializer(loan_disbursement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan_disbursement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)