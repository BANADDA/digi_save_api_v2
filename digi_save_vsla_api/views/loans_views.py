from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import Loans
from digi_save_vsla_api.serializers import LoansSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def loans_list(request):
    data = request.data
    print("Received data:", data.get('groupId'))
    try:
        if request.method == 'POST':
            id=data.get('id'),
            member = data.get('member_id')
            loan_applicant = data.get('loan_applicant')
            group = data.get('groupId')
            loan_purpose = data.get('loan_purpose')
            loan_amount = data.get('loan_amount')
            interest_rate = data.get('interest_rate')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            status = data.get('status')
            loan = Loans(
                id=id,
                member=member,
                loan_applicant=loan_applicant,
                group=group,
                loan_purpose=loan_purpose,
                loan_amount=loan_amount,
                interest_rate=interest_rate,
                start_date=start_date,
                end_date=end_date,
                status=status,
            )
            loan.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Loan created successfully',
            })

        if request.method == 'GET':
            # Get all Loans objects
            loans_list = Loans.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each Loans object excluding 'id' field
            for loan in loans_list:
                data = {
                    'id':loan.id,
                    'member_id': loan.member,
                    'loan_applicant': loan.loan_applicant,
                    'group': loan.group,
                    'loan_purpose': loan.loan_purpose,
                    'loan_amount': loan.loan_amount,
                    'interest_rate': loan.interest_rate,
                    'start_date': loan.start_date,
                    'end_date': loan.end_date,
                    'status': loan.status,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['loans'] = serialized_data.get('loans', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def loans_detail(request, pk):
    try:
        loans = Loans.objects.get(pk=pk)
    except Loans.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoansSerializer(loans)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoansSerializer(loans, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loans.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
