from django import forms
from truckapp.models import Truck

class TruckForm(forms.ModelForm):
           class Meta:
                model=Truck
                fields="__all__"
