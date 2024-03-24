from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('api/update-status/<int:item_id>/',views.update_status,name='update-status'),
    path('api/filter-order-items/',views.filter_order_items,name='filter-order-items'),
    path('api/filter-sales-dashboard/',views.filter_sales_dashboard,name='filter-sales-dashboard')
]
