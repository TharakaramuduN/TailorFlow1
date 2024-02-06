from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import TailorUser
from django import forms

class CreateTailorForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}),required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'email'}),required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone'}),required=True)
    profile = forms.ImageField(label='Profile')
    class Meta:
        model = TailorUser
        fields = ['first_name', 'last_name', 'username', 'email','phone', 'password1', 'password2','profile']
    def __init__(self,*args, **kwargs) -> None:
        super(CreateTailorForm,self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':"Password",'class':'password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':"Confirm Password",'class':'password'})

class TailorLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'input'}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'password'}),required=True)
    class Meta:
        model = TailorUser
        fields = ["username","password"]
    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     super(TailorLoginForm,self).__init__(*args, **kwargs)
    #     self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':"Password",'class':'password'})