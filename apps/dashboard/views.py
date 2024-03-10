from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from apps.orders.models import Order,OrderItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from apps.orders.forms import OrderForm
from django.core.serializers import serialize
from datetime import datetime
# Create your views here.

@login_required
def dashboard(request):
    orders = Order.objects.filter(tailor=request.user)
    order_items = []
    for order in orders:
        items = list(order.items.filter(status='Not-Stitched').order_by('requested_date'))    
        for item in items:
            order_items.append({
                'id':item.id,
                'customer_name':order.customer.first_name,
                'title':item.product.title,
                'requested_date':item.requested_date,
            })
    order_items = sorted(order_items,key=lambda item:item['requested_date'])
    return render(request,'dashboard/dashboard.html',{'order_items':order_items})

def update_status(request,item_id):
    order_item = OrderItem.objects.get(id=item_id)
    order_item.status = 'Stitched'
    order_item.stitched_on = datetime.now()
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