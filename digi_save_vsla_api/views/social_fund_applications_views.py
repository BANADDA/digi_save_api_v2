from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import SocialFundApplications
from digi_save_vsla_api.serializers import SocialFundApplicationsSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def social_fund_applications_list(request):
    data = request.data
    print("Received data:", data.get('group_id'))
    try:
        if request.method == 'POST':
            id=data.get('id'),
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
            meeting_id = data.get('meeting_id')
            submission_date = data.get('submission_date')
            applicant = data.get('applicant')
            group_member_id = data.get('group_member_id')
            amount_needed = data.get('amount_needed')
            social_purpose = data.get('social_purpose')
            repayment_date = data.get('repayment_date')

            social_fund_application = SocialFundApplications(
                id=id,
                group_id=group_id,
                cycle_id=cycle_id,
                meeting_id=meeting_id,
                submission_date=submission_date,
                applicant=applicant,
                group_member=group_member_id,
                amount_needed=amount_needed,
                social_purpose=social_purpose,
                repayment_date=repayment_date,
            )
            social_fund_application.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Social Fund Application created successfully',
            })

        if request.method == 'GET':
            # Get all SocialFundApplications objects
            social_fund_applications_list = SocialFundApplications.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

            # Serialize each SocialFundApplications object excluding 'id' field
            for social_fund_application in social_fund_applications_list:
                data = {
                    'id': social_fund_application.id,
                    'group_id': social_fund_application.group_id,
                    'cycle_id': social_fund_application.cycle_id,
                    'meeting_id': social_fund_application.meeting_id,
                    'submission_date': social_fund_application.submission_date,
                    'applicant': social_fund_application.applicant,
                    'group_member_id': social_fund_application.group_member,
                    'amount_needed': social_fund_application.amount_needed,
                    'social_purpose': social_fund_application.social_purpose,
                    'repayment_date': social_fund_application.repayment_date,
                    # Exclude 'id' field
                }
                # Add the serialized data to the dictionary using the table name as the key
                serialized_data['social_fund_applications'] = serialized_data.get('social_fund_applications', []) + [data]

            # Return the serialized data as JSON
            return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def social_fund_applications_detail(request, pk):
    try:
        social_fund_application = SocialFundApplications.objects.get(pk=pk)
    except SocialFundApplications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialFundApplicationsSerializer(social_fund_application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialFundApplicationsSerializer(social_fund_application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        social_fund_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)