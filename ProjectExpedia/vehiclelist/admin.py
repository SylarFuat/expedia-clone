from django.contrib import admin
from .models import Vehicle, VehicleLocation, VehicleCategory

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(VehicleLocation)
admin.site.register(VehicleCategory)