from django.shortcuts import render, get_object_or_404
from .models import Vehicle, VehicleLocation

# Create your views here.
vehicles = Vehicle.objects.all()


def vehicle_list(request):
    context = {'vehicles': vehicles,}
    return render(request, 'vehiclelist/vlist.html', context)

def vehicle_detail(request, vehicle_id):
    vehicle_details = get_object_or_404(Vehicle, id=vehicle_id)
    context = {
        'vehicle_details': vehicle_details
    }
    return render(request, 'vehiclelist/vdetail.html', context)

def location_list_view(request, location_id):

    location = get_object_or_404(VehicleLocation, id=location_id)
    vehicles = Vehicle.objects.filter(location=location)

    context = {
        'vehicles': vehicles,
        'location': location
    }
    return render(request, 'vehiclelist/location_list.html', context)


    