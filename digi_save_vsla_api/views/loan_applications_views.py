from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import CycleMeeting, GroupForm, GroupMembers, LoanApplications, Meeting
from digi_save_vsla_api.serializers import LoanApplicationsSerializer

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def loan_applications_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            id=data.get('id'),
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
            meeting_id = data.get('meetingId')
            submission_date = data.get('submission_date')
            loan_applicant = data.get('loan_applicant')
            group_member = data.get('group_member_id')
            amount_needed = data.get('amount_needed')
            loan_purpose = data.get('loan_purpose')
            repayment_date = data.get('repayment_date')

            loan_application = LoanApplications(
                id=id,
                group_id=group_id,
                cycle_id=cycle_id,
                meeting_id=meeting_id,
                submission_date=submission_date,
                loan_applicant=loan_applicant,
                group_member=group_member,
                amount_needed=amount_needed,
                loan_purpose=loan_purpose,
                repayment_date=repayment_date,
            )
            loan_application.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Loan Application created successfully',
            })

        if request.method == 'GET':
            # Get all LoanApplications objects
            loan_applications_list = LoanApplications.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each LoanApplications object excluding 'id' field
            for loan_application in loan_applications_list:
                data = {
                    'id': loan_application.id,
                    'group_id': loan_application.group_id,
                    'cycle_id': loan_application.cycle_id,
                    'meetingId': loan_application.meeting_id,
                    'submission_date': loan_application.submission_date,
                    'loan_applicant': loan_application.loan_applicant,
                    'group_member_id': loan_application.group_member,
                    'amount_needed': loan_application.amount_needed,
                    'loan_purpose': loan_application.loan_purpose,
                    'repayment_date': loan_application.repayment_date,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['loan_applications'] = serialized_data.get('loan_applications', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def loan_applications_detail(request, pk):
    try:
        loan_application = LoanApplications.objects.get(pk=pk)
    except LoanApplications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanApplicationsSerializer(loan_application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanApplicationsSerializer(loan_application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)