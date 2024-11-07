from django.urls import path
from . import views

app_name = 'vehiclelist'

urlpatterns = [
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicle_detail/<int:vehicle_id>', views.vehicle_detail, name='vehicle_detail'),
    path('location/<int:location_id>', views.location_list_view, name='location_list'),
]