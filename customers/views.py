from django.shortcuts import render, redirect
from .forms import CustomerForm

# Create your views here.

def newCustomer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            return redirect('/')
        # else:
        #     return render(request,'customers/newCustomer.html',context={'form':form,'errors':errors})
    return render(request,'customers/newCustomer.html',context={'form':form})