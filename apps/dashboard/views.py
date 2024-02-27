from django.shortcuts import render
from django.http import JsonResponse
from apps.orders.models import Order,OrderItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from apps.orders.forms import OrderForm
from django.core.serializers import serialize
# Create your views here.

@login_required
def dashboard(request):
    orders = Order.objects.filter(tailor=request.user)
    return render(request,'dashboard/dashboard.html',{'orders':orders})

def update_status(request,item_id,status):
    order_item = OrderItem.objects.get(id=item_id)
    order_item.status = status
    order_item.save()
    return JsonResponse({'status':'success'})

def filter_products(request):
    filter_by = request.GET.get('filter')
    orders = Order.objects.filter(tailor=request.user)
    order_items = []
    for order in orders:
        order_items.extend(order.items.filter(status=filter_by))

    data = []
    for item in order_items:
        data.append(
            {
                'id':item.id,
                'product':{'title':item.product.title},
                'customer':{'first_name':item.order.customer.first_name},
                'status':item.status
            }
        )
    
    return JsonResponse({'data':data})