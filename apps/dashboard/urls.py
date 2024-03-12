from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('update-status/<int:item_id>/',views.update_status,name='update-status'),
    path('filter-order-items/',views.filter_order_items,name='filter-order-items'),
    path('filter-sales-dashboard/',views.filter_sales_dashboard,name='filter-sales-dashboard')
]
