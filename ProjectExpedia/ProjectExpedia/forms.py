from django import forms
from vehiclelist.us_airports import US_AIRPORTS
from vehiclelist.models import VehicleLocation

class SearchForm(forms.Form):
    pickup_location = forms.ChoiceField(choices=[(loc.id, loc.name) for loc in VehicleLocation.objects.all()], label="Pick-up Location", required=True)
    pickup_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    return_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    pickup_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Pick-Up Time")
    return_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Return Time")
