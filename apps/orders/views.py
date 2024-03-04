from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import OrderForm
from apps.customers.models import Customer
from apps.products.models import Product
from apps.transactions.models import Transaction
from apps.transactions.forms import TransactionForm
from .models import Order, OrderItem
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from datetime import datetime
# Create your views here.

@login_required
def orders(request):
    orders = Order.objects.filter(tailor=request.user)
    paginator = Paginator(orders, 5)
    page_obj = paginator.get_page(1)
    return render(request,'orders/orders.html',{'page_obj':page_obj})

@login_required
def select_customer(request):
    customers = Customer.objects.filter(tailor=request.user)
    return render(request,'orders/select_customer.html',context={'customers':customers})

@login_required
def select_products(request,customer_id):
    products = Product.objects.filter(tailor=request.user)
    return render(request,'orders/select_products.html',context={'products':products,'customer_id':customer_id})

@login_required
def checkout(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    print(customer_id)
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        selected_products = Product.objects.filter(tailor=request.user,id__in=selected_product_ids)
        checkout_origin = request.POST.get('checkout','')
        OrderItemFormSet = modelformset_factory(OrderItem,fields='__all__',extra=len(selected_products))
        transaction_form = TransactionForm()
        if checkout_origin == 'true': 
            amount = int(request.POST.get('amount'))
            order_form = OrderForm(request.POST)
            formset = OrderItemFormSet(request.POST)
            transaction_form = TransactionForm(request.POST)
            # print(order_form)
            
            if order_form.is_valid() and formset.is_valid() and transaction_form.is_valid():
                order = order_form.save(commit=False)
                order.save()
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.order = order
                    instance.save()
                if amount > 0:
                    transaction = transaction_form.save(commit=False)
                    transaction.order = order
                    transaction.save()
                return redirect('/orders')
            else:
                print(order_form.errors)
        else:
            order_id = generate_order_id(customer_id)
            order_form = OrderForm(initial={'tailor':request.user,'customer':customer,'items_count':len(selected_product_ids),'id':order_id})
            formset = OrderItemFormSet(queryset=OrderItem.objects.none(),initial=[{'product':product} for product in selected_products])
            return render(request,'orders/checkout.html',{
                'selected_products':selected_products,
                'customer':customer,
                'formset' : formset,
                'order_form':order_form,
                'transaction_form':transaction_form,
            })
    else:
        print("it's a get method")
        
def generate_order_id(customer_id):
    timestamp = datetime.now().strftime("%y%m%d%H%M%S")
    order_id = f"{timestamp}{customer_id}"
    return order_id

@login_required      
def order_details(request,order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    OrderItemFormSet = modelformset_factory(OrderItem,fields='__all__',extra=0)
    transaction_form = TransactionForm()
    transactions = Transaction.objects.filter(order=order)
    print(transactions)
    amount_paid = 0
    for transaction in transactions:
        amount_paid += transaction.amount

    max_input_value = order.total_price - amount_paid

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, queryset=order_items)
        transaction_form = TransactionForm(request.POST)
        amount = int(request.POST.get('amount'))
        if form.is_valid() and formset.is_valid() and transaction_form.is_valid():
            order = form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.order = order
                instance.save()
            if amount > 0:
                transaction = transaction_form.save(commit=False)
                transaction.tailor = request.user
                transaction.order = order
                transaction.save()
            return redirect('/orders')
        else:
            print(transaction_form.errors,form.errors,formset.errors)
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(queryset=order_items)
    
    return render(request, 'orders/order_details.html', {
        'form': form, 'formset': formset, 
        'order': order,'transaction_form':transaction_form,
        'amount_paid':amount_paid,
        'max_input_value':max_input_value,
        })

@login_required
def filter_orders(request):
    search_query = request.GET.get('search','')
    orders = Order.objects.filter(tailor=request.user)
    if search_query:
        orders = orders.filter(
            Q(customer__first_name__icontains=search_query) |
            Q(id__icontains=search_query)
        )
    paginator = Paginator(orders,5)
    page_num = request.GET.get('page')
    print(page_num)
    page_obj = paginator.get_page(page_num)
    orders_data = list(page_obj.object_list.values('id','total_price', 'items_count', 'customer__first_name'))
    print(orders_data)
    page_data = {
        'number':page_obj.number,
        'num_pages':page_obj.paginator.num_pages,
        'has_next':page_obj.has_next(),
        'has_previous':page_obj.has_previous(),
        'previous_page_number':page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number':page_obj.next_page_number() if page_obj.has_next() else None,

    }
    return JsonResponse({'page_obj':page_data,'orders':orders_data})