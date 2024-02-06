from django import forms
from .models import Customer, Measurements

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = "__all__"