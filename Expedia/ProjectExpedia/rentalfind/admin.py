from django.contrib import admin
from .models import VehicleCategory, Vehicle, Location

# Register your models here.
admin.site.register(VehicleCategory)
admin.site.register(Vehicle)
admin.site.register(Location)