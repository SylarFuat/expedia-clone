from django.db import models
from django import forms
from .us_airports import US_AIRPORTS

from PIL import Image

class VehicleLocation(models.Model):

    name = models.CharField(max_length=100)
    LOCATION_CHOICES = [(code, f"{name} ({code})") for name, code in US_AIRPORTS.items()]
    location = models.CharField(max_length=150, choices=LOCATION_CHOICES)

    def __str__(self):
        return self.name
    
class VehicleCategory(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    price = models.CharField(max_length=50, default=0)
    imagefield = models.ImageField(upload_to='images/', blank=True, null=True, default='')
    location = models.ForeignKey(VehicleLocation, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE, default=None)

    is_available = models.BooleanField(default=True)
    free_cancellation = models.BooleanField(default=False)
    unlimited_milage = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}" 

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'year', 'price', 'location', 'category', 'is_available']


