# views/group_form_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import AssignedPositions, ConstitutionTable, CycleSchedules, GroupForm, GroupMembers, GroupProfile, Users
from digi_save_vsla_api.serializers import GroupFormSerializer

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def group_form_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            id=data.get('id'),
            group_profile_id = data.get('group_profile_id')
            group_id = data.get('group_id')
            logged_in_users_id = data.get('logged_in_user_id')
            constitution_id = data.get('constitution_id')
            cycle_schedule_id = data.get('cycle_schedule_id')
            group_member_id = data.get('group_member_id')
            assigned_position_id = data.get('assigned_position_id')

            # Get the related instances based on their IDs
            # group_profile = GroupProfile.objects.get(profile_id=group_profile_id)
            # logged_in_users = Users.objects.get(users_id=logged_in_users_id)
            # constitution = ConstitutionTable.objects.get(constitution_id=constitution_id)
            # cycle_schedule = CycleSchedules.objects.get(schedule_id=cycle_schedule_id)
            # group_member = GroupMembers.objects.get(member_id=group_member_id)
            # assigned_position = AssignedPositions.objects.get(assign_id=assigned_position_id)

            group_form = GroupForm(
                id=id,
                group_profile_id=group_profile_id,
                group_id=group_id,
                logged_in_users_id=logged_in_users_id,
                constitution_id=constitution_id,
                cycle_schedule_id=cycle_schedule_id,
                group_member_id=group_member_id,
                assigned_position_id=assigned_position_id,
            )
            group_form.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Group form created successfully',
            })

        if request.method == 'GET':
            group_forms = GroupForm.objects.all()
            group_form_data = {'group_form': []}  # Initialize an empty list for group_form

            for form in group_forms:
                data = {
                    'id':form.id,
                    'group_profile_id': form.group_profile_id,
                    'group_id': form.group_id,
                    'logged_in_user_id': form.logged_in_users_id,
                    'constitution_id': form.constitution_id,
                    'cycle_schedule_id': form.cycle_schedule_id,
                    'group_member_id': form.group_member_id,
                    'assigned_position_id': form.assigned_position_id,
                }
                group_form_data['group_form'].append(data)  # Append data for each form

        return JsonResponse(group_form_data, safe=False)


    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def group_form_detail(request, pk):
    try:
        group_form = GroupForm.objects.get(pk=pk)
    except GroupForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupFormSerializer(group_form)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupFormSerializer(group_form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
