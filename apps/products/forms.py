from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model = Product
        fields = "__all__"