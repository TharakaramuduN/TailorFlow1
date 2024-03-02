from django.shortcuts import render
from .models import Transaction
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def transactions(request):
    print(request.path)
    transactions = Transaction.objects.filter(tailor=request.user)
    return render(request,'transactions/transactions.html',{'transactions':transactions})