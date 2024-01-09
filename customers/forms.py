from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    # city = forms.CharField(label='Village/City')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'floating_first_name','class':'block pt-4 pb-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'floating_last_name','class':'block pt-4 pb-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'floating_email','class':'block pt-4 pb-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'id':'floating_phone','class':' block pt-4 pb-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'id':'floating_city','class':'block pt-4 pb-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    # profile = forms.ImageField(widget=forms.ImageField(attrs={'id':'floating_profile','name':'floating_profile','class':'block py-5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    class Meta:
        model = Customer
        fields = ['profile']
    # def __init__(self,*args, **kwargs):
    #     super(CustomerForm,self).__init__(*args, **kwargs)
    #     self.fields['profile'].widget = forms.ImageField(attrs={'id':'floating_profile','name':'floating_profile','class':'block py-5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'})
