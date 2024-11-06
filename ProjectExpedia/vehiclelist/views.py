from django.shortcuts import render, get_object_or_404
from .models import Vehicle

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

def tryhard():
    pass


    