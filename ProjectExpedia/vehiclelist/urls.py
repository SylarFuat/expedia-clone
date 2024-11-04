from django.urls import path
from . import views

urlpatterns = [
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('vehicle_detail/<int:vehicle_id>', views.vehicle_detail, name='vehicle_detail'),
]