# views/group_form_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import AssignedPositions, ConstitutionTable, CycleSchedules, GroupForm, GroupMembers, GroupProfile, Users
from digi_save_vsla_api.serializers import GroupFormSerializer

@api_view(['GET', 'POST'])
def group_form_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            group_profile = data.get('group_profile_id')
            logged_in_users = data.get('logged_in_users_id')
            constitution = data.get('constitution_id')
            cycle_schedule = data.get('cycle_schedule_id')
            group_member = data.get('group_member_id')
            assigned_position = data.get('assigned_position_id')

            # Get the related instances based on their IDs
            group_profile_id = GroupProfile.objects.get(id=group_profile)
            logged_in_users = Users.objects.get(id=logged_in_users)
            constitution = ConstitutionTable.objects.get(id=constitution)
            cycle_schedule = CycleSchedules.objects.get(id=cycle_schedule)
            group_member = GroupMembers.objects.get(id=group_member)
            # assigned_position = AssignedPositions.objects.get(id=assigned_position_id)

            group_form = GroupForm(
                group=group_profile_id,
                logged_in_users=logged_in_users,
                constitution=constitution,
                cycle_schedule=cycle_schedule,
                group_member=group_member,
                assigned_position=assigned_position,
            )
            group_form.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Group form created successfully',
            })

        if request.method == 'GET':
            group_forms = GroupForm.objects.all()
            group_form_data = []
            for group_form in group_forms:
                group_form_data.append({
                    'group_profile_id': group_form.group,
                    'logged_in_users_id': group_form.logged_in_users,
                    'constitution_id': group_form.constitution,
                    'cycle_schedule_id': group_form.cycle_schedule,
                    'group_member_id': group_form.group_member,
                    'assigned_position_id': group_form.assigned_position,
                })
            return JsonResponse({
                'status': 'success',
                'group_forms': group_form_data,
            })

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
