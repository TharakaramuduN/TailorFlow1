from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':' border-b-2 border-yellow-500 bg-black focus:outline-none'}))
    last_name = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':' border-b-2 border-yellow-500 bg-black focus:outline-none'}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':' border-b-2 border-yellow-500 bg-black focus:outline-none'}))
    city = forms.CharField(label="City",widget=forms.TextInput(attrs={'class':' border-b-2 border-yellow-500 bg-black focus:outline-none'}))
    phone = forms.CharField(label="Phone",widget=forms.TextInput(attrs={'class':' border-b-2 border-yellow-500 bg-black focus:outline-none'}))
    class Meta:
        model = Customer
        fields = ['first_name','last_name','email','city','phone','profile'] 