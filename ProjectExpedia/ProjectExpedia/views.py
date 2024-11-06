from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from vehiclelist.models import Vehicle
from .forms import SearchForm

def home(request):
    vehicles = Vehicle.objects.all()
    # List comphrension
    # getlax_us = [(code, name) for name, code in US_AIRPORTS.items() if code.startswith('L')]

    context = {
        'vehicles': vehicles,
    }

    return render(request, 'index.html', context)

def search_view(request):

    form = SearchForm(request.POST or None)
    context = {'form': form} 

    if request.method =='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            pickup_location = form.cleaned_data['pickup_location']
            pickup_date = form.cleaned_data['pickup_date']
            return_date = form.cleaned_data['return_date']
            pickup_time = form.cleaned_data['pickup_time']
            return_time = form.cleaned_data['return_time']

            context = {
                'pickup_location': pickup_location,
                'pickup_date': pickup_date,
                'return_date': return_date,
                'pickup_time': pickup_time,
                'return_time': return_time,
            }
        return render(request, 'search_result.html', context)
    else:
        form = SearchForm()
    
    return redirect('home')