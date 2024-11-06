from django import forms
from vehiclelist.us_airports import US_AIRPORTS

class SearchForm(forms.Form):
    pickup_location = forms.ChoiceField(choices=US_AIRPORTS, label="Pick-up Location")
    pickup_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    return_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    pickup_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Pick-Up Time")
    return_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Return Time")
