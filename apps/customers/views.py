from django.shortcuts import render, redirect
from .forms import CustomerForm,MeasurementsForm
from django.db import IntegrityError
from .models import Customer, Measurements
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.conf import settings

@login_required
def new_customer(request):
    origin = request.GET.get('origin','')
    form = CustomerForm() 

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)

        if form.is_valid():
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            if Customer.objects.filter(tailor=request.user).filter(phone=phone):
                form.add_error('phone','Customer with this phone already exists')
            if Customer.objects.filter(tailor=request.user).filter(email=email):
                form.add_error('email','Customer with this email already exists')
            else:
                try:
                    customer = form.save(commit=False)
                    customer.tailor = request.user
                    customer.save()
                    if origin:
                        return redirect(f'/add-measurements/{customer.id}/?next=select-products')
                    return redirect(add_measurements,customer_id=customer.id)
                except IntegrityError as e:
                    # Handle any potential IntegrityError that may occur during the save
                    print(e)
                    form.add_error(None, 'A database integrity error occurred.')

    return render(request, 'customers/new_customer.html', context={'form': form})

@login_required
def edit_customer(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.tailor = request.user
            customer.save()
            return redirect(customer_details,customer_id=customer_id)
    else:
        form = CustomerForm(instance=customer)
    return render(request,'customers/edit_customer.html',context={'form':form})

# queryset = Customer.objects.all()
# for obj in queryset:
#     print(obj)

@login_required
def customers(request):
    tailor = request.user
    customers = Customer.objects.filter(tailor=tailor)
    return render(request,'customers/customers.html',context={'customers':customers})

@login_required
def customer_details(request,customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        measurements = Measurements.objects.filter(customer=customer).first()
        form = MeasurementsForm(instance=measurements) if measurements else None
        if request.method == 'POST':
            customer.delete()
            return redirect('/customers')
        return render(request,'customers/customer_details.html',context={'customer':customer,'form':form})
    except Customer.DoesNotExist:
        return HttpResponse('Customer does not exist.')

@login_required
def add_measurements(request,customer_id):
    next_url = request.GET.get('next','')
    customer = Customer.objects.get(id=customer_id)
    form = MeasurementsForm()
    if request.method == "POST":
        form = MeasurementsForm(request.POST)
        if form.is_valid():
            measurements = form.save(commit=False)
            measurements.customer = customer
            measurements.save()
            if next_url:
                return redirect('select-products',customer_id=customer_id)
            return redirect(customer_details,customer_id=customer_id)
    return render(request,'customers/add_measurements.html',context={'form':form,'customer':customer})

@login_required
def edit_measurements(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    measurements = Measurements.objects.get(customer=customer)
    form = MeasurementsForm(instance=measurements)
    if request.method == "POST":
        form = MeasurementsForm(request.POST,instance=measurements)
        if form.is_valid():
            form.save()
            return redirect(customer_details,customer_id=customer_id)
    return render(request,'customers/edit_measurements.html',context={'customer':customer,'form':form})

@login_required
def filter_customers(request):
    search = request.GET.get('search','')
    gender = request.GET.get('gender','')
    sortby = request.GET.get('sortby','')

    queryset = Customer.objects.filter(tailor=request.user)

    if search:
        queryset = queryset.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search) |
            Q(city__icontains=search) |
            Q(phone__icontains=search)
        ).distinct()
    
    if gender:
        queryset = queryset.filter(gender = gender)
    
    if sortby:
        queryset = queryset.order_by(sortby)

    customers_data = list(queryset.values())
    for customer in customers_data:
        customer['profile'] = settings.MEDIA_URL + str(customer['profile'])
    return JsonResponse({'customers':customers_data})
