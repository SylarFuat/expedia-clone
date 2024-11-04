from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from vehiclelist.models import Vehicle
from vehiclelist.us_airports import US_AIRPORTS

def home(request):
    vehicles = Vehicle.objects.all()
    # List comphrension
    # getlax_us = [(code, name) for name, code in US_AIRPORTS.items() if code.startswith('L')]

    context = {
        'vehicles': vehicles,
    }

    return render(request, 'index.html', context)

