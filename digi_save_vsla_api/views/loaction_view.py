from django.http import JsonResponse
from digi_save_vsla_api.models import *

def get_location_data(request):
    if request.method == 'GET':
        districts = District.objects.all().values('id', 'name')
        subcounties = Subcounty.objects.all().values('id', 'name')
        villages = Village.objects.all().values('id', 'name')

        location_data = {
            'districts': list(districts),
            'subcounties': list(subcounties),
            'villages': list(villages)
        }

        return JsonResponse(location_data)
    else:
        return JsonResponse({'message': 'Unsupported method'}, status=405)
