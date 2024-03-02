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
# Create your views here.

@login_required
def orders(request):
    orders = Order.objects.filter(tailor=request.user)
    return render(request,'orders/orders.html',{'orders':orders})

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
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        selected_products = Product.objects.filter(tailor=request.user,id__in=selected_product_ids)
        checkout_origin = request.POST.get('checkout','')
        OrderItemFormSet = modelformset_factory(OrderItem,fields='__all__',extra=len(selected_products))
        transaction_form = TransactionForm()
        if checkout_origin == 'true':
            order_form = OrderForm(request.POST)
            formset = OrderItemFormSet(request.POST)
            transaction_form = TransactionForm(request.POST)
            if order_form.is_valid() and formset.is_valid() and transaction_form.is_valid():
                order = order_form.save()
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.order = order
                    instance.save()
                transaction = transaction_form.save(commit=False)
                transaction.order = order
                transaction.save()
                return redirect('/orders')
            else:
                print(formset.errors)
        else:
            order_form = OrderForm(initial={'tailor':request.user,'customer':customer,'items_count':len(selected_product_ids)})
            formset = OrderItemFormSet(queryset=OrderItem.objects.none(),initial=[{'product':product} for product in selected_products])
            return render(request,'orders/checkout.html',{
                'selected_products':selected_products,
                'customer':customer,
                'formset' : formset,
                'order_form':order_form,
                'transaction_form':transaction_form,
            })

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
        if form.is_valid() and formset.is_valid() and transaction_form.is_valid():
            order = form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.order = order
                instance.save()
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