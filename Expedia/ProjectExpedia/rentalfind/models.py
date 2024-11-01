from django.db import models
from django import forms

# Create your models here.
class VehicleCategory(models.Model):
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)  # E.g., "Los Angeles"
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vehicle(models.Model):

    name = models.CharField(max_length=100)
    v_model = models.CharField(max_length=50)
    year = models.CharField(max_length=20)
    category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE, related_name="vehicles")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="vehicles")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'v_model', 'location', 'category', 'is_available']