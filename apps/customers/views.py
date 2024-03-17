from django.shortcuts import render, redirect
from .forms import CustomerForm,MeasurementsForm
from django.db import IntegrityError
from .models import Customer, Measurements
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.conf import settings
from django.core.paginator import Paginator

@login_required
def new_customer(request):
    # origin = request.GET.get('origin','')
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
                    # if origin:
                    #     return redirect(f'/add-measurements/{customer.id}')
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
    pagination = Paginator(customers,7)
    page_obj = pagination.get_page(1)
    return render(request,'customers/customers.html',context={'page_obj':page_obj,'title':'Customers'})

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
    # next_url = request.GET.get('next','')
    customer = Customer.objects.get(id=customer_id)
    form = MeasurementsForm()
    if request.method == "POST":
        form = MeasurementsForm(request.POST)
        if form.is_valid():
            measurements = form.save(commit=False)
            measurements.customer = customer
            measurements.save()
            # if next_url:
            return redirect('select-products',customer_id=customer_id)
            # return redirect(customer_details,customer_id=customer_id)
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

    customers = Customer.objects.filter(tailor=request.user)

    if search:
        customers = customers.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search) |
            Q(city__icontains=search) |
            Q(phone__icontains=search)
        ).distinct()
    
    if gender:
        customers = customers.filter(gender = gender)
    
    if sortby:
        customers = customers.order_by(sortby)
    
    pagination = Paginator(customers,7)
    page_num = request.GET.get('page')
    page_obj = pagination.get_page(page_num)
    page_data = {
        'number':page_obj.number,
        'num_pages':page_obj.paginator.num_pages,
        'has_next':page_obj.has_next(),
        'has_previous':page_obj.has_previous(),
        'previous_page_number':page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number':page_obj.next_page_number() if page_obj.has_next() else None,

    }
    customers_data = list(page_obj.object_list.values())
    for customer in customers_data:
        customer['profile'] = settings.MEDIA_URL + str(customer['profile'])
    return JsonResponse({'customers':customers_data,'page_obj':page_data})
