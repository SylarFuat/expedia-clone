from django.shortcuts import render, get_object_or_404, redirect
from vehiclelist.models import Vehicle, VehicleLocation
from .forms import SearchForm


def home(request):
    vehicles = Vehicle.objects.all()
    form = SearchForm()

    context = {
        'vehicles': vehicles,
        'form': form,
    }
    return render(request, 'index.html', context)

# Search vehicle/list/detail
def search_view(request):

    form = SearchForm(request.POST or None)
    locations = VehicleLocation.objects.all()
    context = {'form': form, 'locations': locations}

    if request.method =='POST' and form.is_valid(): 
        pickup_location_id = form.cleaned_data['pickup_location']
        pickup_location = VehicleLocation.objects.get(id=pickup_location_id)
        pickup_date = form.cleaned_data['pickup_date']
        return_date = form.cleaned_data['return_date']
        pickup_time = form.cleaned_data['pickup_time']
        return_time = form.cleaned_data['return_time']

        vehicles = Vehicle.objects.filter(location=pickup_location)
        reservation_days = (return_date - pickup_date).days

        for vehicle in vehicles:
            vehicle.total_price = float(vehicle.price) * reservation_days
        # cheapest_opt = vehicles.order_by('price').first()
        # highest_opt = vehicles.order_by('-rating').first()

        context = {
            'pickup_location': pickup_location,
            'pickup_date': pickup_date,
            'return_date': return_date,
            'pickup_time': pickup_time,
            'return_time': return_time,
            'vehicles': vehicles,
            'reservation_days': reservation_days,
            'locations': locations
            # 'cheapest_opt': cheapest_opt,
            # 'highest_opt': highest_opt,
        }

        return render(request, 'search_result.html', context)
    
    return render(request, 'index.html', context)