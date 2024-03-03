from django.urls import path
from . import views

urlpatterns = [
    path('orders/',views.orders,name='orders'),
    path('select-customer/',views.select_customer,name='select-customer'),
    path('select-products/<int:customer_id>/',views.select_products,name='select-products'),
    path('checkout/<int:customer_id>/',views.checkout,name='checkout'),
    path('order-details/<int:order_id>/',views.order_details,name='order-details'),
    path('filter-orders/',views.filter_orders,name='filter-orders'),
]
