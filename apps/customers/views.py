from django.shortcuts import render, redirect
from .forms import CustomerForm
from django.db import IntegrityError
from .models import Customer  # Import your Customer model

def newCustomer(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)

        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            # Check for uniqueness manually before saving
            if Customer.objects.filter(email=email).exists():
                form.add_error('email', 'This email address is already in use.')
            elif Customer.objects.filter(phone=phone).exists():
                form.add_error('phone', 'This phone number is already in use.')
            else:
                # If no uniqueness issues, create and save the Customer instance
                try:
                    customer_instance = Customer(
                        first_name=form.cleaned_data['first_name'],
                        last_name=form.cleaned_data['last_name'],
                        email=email,
                        phone=phone,
                        city=form.cleaned_data['city'],
                        profile=form.cleaned_data['profile']
                    )
                    customer_instance.save()

                    return redirect('/')
                except IntegrityError as e:
                    # Handle any potential IntegrityError that may occur during the save
                    print(e)
                    form.add_error(None, 'A database integrity error occurred.')

    return render(request, 'customers/newCustomer.html', context={'form': form})