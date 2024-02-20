from django.shortcuts import render,HttpResponse,redirect
from .forms import OrderForm
from apps.customers.models import Customer
from apps.products.models import Product
from .models import Order, OrderItem
from django.forms import modelformset_factory
from django import forms
# Create your views here.

def orders(request):
    orders = Order.objects.filter(tailor=request.user)
    return render(request,'orders/orders.html',{'orders':orders})

def select_customer(request):
    customers = Customer.objects.filter(tailor=request.user)
    return render(request,'orders/select_customer.html',context={'customers':customers})

def select_products(request,customer_id):
    products = Product.objects.filter(tailor=request.user)
    return render(request,'orders/select_products.html',context={'products':products,'customer_id':customer_id})

def checkout(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        selected_products = Product.objects.filter(tailor=request.user,id__in=selected_product_ids)
        checkout_origin = request.POST.get('checkout','')
        OrderItemFormSet = modelformset_factory(OrderItem,fields='__all__',extra=len(selected_products))
        if checkout_origin == 'true':
            order_form = OrderForm(request.POST)
            formset = OrderItemFormSet(request.POST)
            if order_form.is_valid() and formset.is_valid():
                order = order_form.save()
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.order = order
                    instance.save()
                return redirect('/orders')
            else:
                print(formset.errors,'HELLLLLLOOOOO')
        else:
            order_form = OrderForm(initial={'tailor':request.user,'customer':customer})
            formset = OrderItemFormSet(queryset=OrderItem.objects.none(),initial=[{'product':product} for product in selected_products])
            return render(request,'orders/checkout.html',{
                'selected_products':selected_products,
                'customer':customer,
                'formset' : formset,
                'order_form':order_form
            })
        
def order_details(request,order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request,'orders/order_details.html',{
        'order':order,
        'order_items':order_items
    })