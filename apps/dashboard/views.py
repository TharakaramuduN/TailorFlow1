from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from apps.orders.models import Order,OrderItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from apps.orders.forms import OrderForm
from django.core.serializers import serialize
from datetime import datetime,timedelta
from apps.transactions.models import Transaction
from apps.customers.models import Customer
# Create your views here.

@login_required
def dashboard(request):
    orders = Order.objects.filter(tailor=request.user)
    customers = Customer.objects.filter(tailor=request.user)
    transactions = Transaction.objects.filter(tailor=request.user)
    sales = sum([transaction.amount for transaction in transactions])
    total_order_items = 0
    delivered = 0
    urgent = 0
    stitched = 0
    prepaid,postpaid = 0,0
    prepaid += len(orders.filter(payment_type='PRE'))
    postpaid += len(orders.filter(payment_type='POST'))
    order_items = []
    for order in orders:
        total_order_items += len(order.items.all())
        delivered += len(order.items.filter(status='Delivered'))
        stitched += len(order.items.filter(status='Stitched'))
        urgent += len(order.items.filter(urgent=True,status='Not-Stitched'))
        items = list(order.items.filter(status='Not-Stitched').order_by('requested_date'))    
        for item in items:
            order_items.append({
                'id':item.id,
                'customer_name':order.customer.first_name,
                'title':item.product.title,
                'requested_date':item.requested_date,
            })
    order_items = sorted(order_items,key=lambda item:item['requested_date'])
    print(delivered)
    return render(request,'dashboard/dashboard.html',{'order_items':order_items,'total_orders':len(orders),
                                                      'sales':sales,'total_customers':len(customers),
                                                      'delivered':delivered,'total_order_items':total_order_items,
                                                      'urgent':urgent,'stitched':stitched,'prepaid':prepaid,'postpaid':postpaid,
                                                      'title':'Dashboard'})

def update_status(request,item_id):
    order_item = OrderItem.objects.get(id=item_id)
    order_item.status = 'Stitched'
    order_item.stitched_on = datetime.now().date()
    order_item.save()
    return JsonResponse({'status':'success'})

def filter_order_items(request):
    filter_by = request.GET.get('filter')
    urgent = request.GET.get('urgent','')
    orders = Order.objects.filter(tailor=request.user)
    order_items = []
    for order in orders:
        items = order.items.all()
        if urgent == 'true':
            items = list(items.filter(urgent=True,status='Not-Stitched').order_by('requested_date'))
        else:
            items = list(items.filter(status=filter_by).order_by('requested_date'))
        for item in items:
            order_items.append({
                'id':item.id,
                'customer_name':order.customer.first_name,
                'title':item.product.title,
                'requested_date':item.requested_date,
                'stitched_on':item.stitched_on
            })
    if filter_by == 'Stitched':
        order_items = sorted(order_items,key=lambda item:item['stitched_on'],reverse=True)
    return JsonResponse({'order_items':order_items})

def filter_sales_dashboard(request):
    filter_by_date = request.GET.get('filter_by_date')
    orders = Order.objects.filter(tailor=request.user)
    customers = Customer.objects.filter(tailor=request.user)
    transactions = Transaction.objects.filter(tailor=request.user)
    if filter_by_date == 'Total':
        orders = orders
        customers = customers
        transactions = transactions
    if filter_by_date == 'Today':
        orders = orders.filter(order_date_time__date = datetime.today())
        customers = customers.filter(created_at__date = datetime.today())
        transactions = transactions.filter(date_time__date=datetime.today())
    elif filter_by_date == 'last_7_days':
        delta = timedelta(days=7)
        start_date = datetime.now() - delta
        orders = orders.filter(order_date_time__gte = start_date)
        customers = customers.filter(created_at__gte = start_date)
        transactions = transactions.filter(date_time__gte = start_date)
    elif filter_by_date == 'this_month':
        month = datetime.now().month
        year = datetime.now().year
        orders = orders.filter(order_date_time__month = month,order_date_time__year=year)
        customers = customers.filter(created_at__month = month,created_at__year=year)
        transactions = transactions.filter(date_time__month=month,date_time__year=year)
    elif filter_by_date == 'this_year':
        year = datetime.now().year
        orders = orders.filter(order_date_time__year=year)
        customers = customers.filter(created_at__year=year)
        transactions = transactions.filter(date_time__year=year)

    orders_count = len(orders)
    customers_count = len(customers)
    sales_count = 0
    items_count = 0
    prepaid_count = len(orders.filter(payment_type='PRE'))
    postpaid_count = len(orders.filter(payment_type='POST'))

    for order in orders:
        items_count += len(order.items.all())
    
    sales_count += sum([transaction.amount for transaction in transactions])

    return JsonResponse({'orders_count':orders_count,'customers_count':customers_count,
                         'sales_count':sales_count,'items_count':items_count,
                         'prepaid_count':prepaid_count,'postpaid_count':postpaid_count})