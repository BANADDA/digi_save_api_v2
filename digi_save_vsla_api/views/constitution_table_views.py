from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import ConstitutionTable, GroupProfile
from digi_save_vsla_api.serializers import ConstitutionTableSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def constitution_table_list(request):
    print("Received data:", request.data)
    data = request.data
    try:
        if request.method == 'POST':
            id=data.get('id'),
            group_id = data.get('group_id')
            hasConstitution = data.get('hasConstitution')
            constitutionFiles = data.get('constitutionFiles')
            usesGroupShares = data.get('usesGroupShares')
            shareValue = data.get('shareValue')
            maxSharesPerMember = data.get('maxSharesPerMember')
            minSharesRequired = data.get('minSharesRequired')
            frequencyOfContributions = data.get('frequencyOfContributions')
            offersLoans = data.get('offersLoans')
            maxLoanAmount = data.get('maxLoanAmount')
            interestRate = data.get('interestRate')
            interestMethod = data.get('interestMethod')
            loanTerms = data.get('loanTerms')
            registrationFee = data.get('registrationFee')
            selectedCollateralRequirements = data.get('selectedCollateralRequirements')

            # Get the GroupProfile instance based on the group_id
            # group_profile = GroupProfile.objects.get(profile_id=group_id)

            constitution = ConstitutionTable(
                id=id,
                group_id=group_id,
                hasConstitution=hasConstitution,
                constitutionFiles=constitutionFiles,
                usesGroupShares=usesGroupShares,
                shareValue=shareValue,
                maxSharesPerMember=maxSharesPerMember,
                minSharesRequired=minSharesRequired,
                frequencyOfContributions=frequencyOfContributions,
                offersLoans=offersLoans,
                maxLoanAmount=maxLoanAmount,
                interestRate=interestRate,
                interestMethod=interestMethod,
                loanTerms=loanTerms,
                registrationFee=registrationFee,
                selectedCollateralRequirements=selectedCollateralRequirements,
            )
            constitution.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Constitution created successfully',
            })

        if request.method == 'GET':
            # Get all ConstitutionTable objects
            constitution_tables = ConstitutionTable.objects.all()

            # Create a list to store the serialized data
            serialized_data = {}

        # Serialize each ConstitutionTable object excluding 'id' and 'sync_flag'
        for constitution_table in constitution_tables:
            data = {
                'id':constitution_table.id,
                'group_id': constitution_table.group_id,  # assuming you want the group_id's id
                'hasConstitution': constitution_table.hasConstitution,
                'constitutionFiles': constitution_table.constitutionFiles,
                'usesGroupShares': constitution_table.usesGroupShares,
                'shareValue': constitution_table.shareValue,
                'maxSharesPerMember': constitution_table.maxSharesPerMember,
                'minSharesRequired': constitution_table.minSharesRequired,
                'frequencyOfContributions': constitution_table.frequencyOfContributions,
                'offersLoans': constitution_table.offersLoans,
                'maxLoanAmount': constitution_table.maxLoanAmount,
                'interestRate': constitution_table.interestRate,
                'interestMethod': constitution_table.interestMethod,
                'loanTerms': constitution_table.loanTerms,
                'registrationFee': constitution_table.registrationFee,
                'selectedCollateralRequirements': constitution_table.selectedCollateralRequirements,
                # Exclude 'id' and 'sync_flag' fields
            }

            # Add the serialized data to the dictionary using the table name as the key
            serialized_data['constitution_table'] = serialized_data.get('constitution_table', []) + [data]

        # Return the serialized data as JSON
        return JsonResponse(serialized_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def constitution_table_detail(request, pk):
    try:
        constitution_table = ConstitutionTable.objects.get(pk=pk)
    except ConstitutionTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConstitutionTableSerializer(constitution_table)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConstitutionTableSerializer(constitution_table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        constitution_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
