# views/group_members_views.py
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from digi_save_vsla_api.models import GroupMembers, GroupProfile, Users
from digi_save_vsla_api.serializers import GroupMembersSerializer

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def group_members_list(request):
    data = request.data
    print("Received data:", data)
    try:
        if request.method == 'POST':
            
            print("Received data:", data)
            group_id = data.get('group_id')
            user_id = data.get('user_id')

            #  # Get the GroupProfile instance based on the group_id
            # group_id = GroupProfile.objects.get(profile_id=group_id)
            # user_id = Users.objects.get(users_id=user_id)


            group_members = GroupMembers(
                group_id=group_id,
                user_id=user_id,
            )
            group_members.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Group members added successfully',
            })

        if request.method == 'GET':
            # Get all GroupMembers objects
            group_members = GroupMembers.objects.all()

            # Create a list to store the serialized data
            serialized_data = {'group_members': []}

            # Serialize each GroupMembers object excluding 'id' and 'sync_flag'
            for member in group_members:
                data = {
                    'user_id': member.user_id,  # assuming you want the user_id's id
                    'group_id': member.group_id,  # assuming you want the group_id's id
                    # Exclude 'id' and 'sync_flag' fields
                }
                # Append each serialized data to the list under 'group_members' key
                serialized_data['group_members'].append(data)

        # Return the serialized data as JSON
        return JsonResponse(serialized_data, safe=False)

    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

@api_view(['GET', 'PUT', 'DELETE'])
def group_members_detail(request, pk):
    try:
        group_member = GroupMembers.objects.get(pk=pk)
    except GroupMembers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupMembersSerializer(group_member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupMembersSerializer(group_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
