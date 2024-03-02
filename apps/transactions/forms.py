from .models import Transaction
from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
    