from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.db import IntegrityError

# Create your views here.

def newCustomer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                form.save()
                return redirect('/')
            except IntegrityError as e:
                print(e)
                if 'unique constraint' in str(e).lower() and 'email' in str(e).lower():
                    form.add_error('email','This email address is already in use.')
                elif 'unique constraint' in str(e).lower() and 'phone' in str(e).lower():
                    form.add_error('phone','This phone number is already in use.')
                else:
                    form.add_error(None,'A database integrity error occured.')
        # else:
        #     return render(request,'customers/newCustomer.html',context={'form':form,'errors':errors})
    return render(request,'customers/newCustomer.html',context={'form':form})