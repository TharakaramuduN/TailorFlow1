from django.shortcuts import render
from django.urls import path, include
from . import views

# Create your views here.

urlpatterns = [
    path('new-customer/',views.new_customer,name='new-customer'),
    path('customers/',views.customers,name='customers'),
    path('add-measurements/<int:customer_id>/',views.add_measurements,name='add-measurements'),
    path('edit-customer/<int:customer_id>/',views.edit_customer,name='edit-customer'),
    path('customer-details/<int:customer_id>/',views.customer_details,name="customer-details"),
    path('edit-measurements/<int:customer_id>/',views.edit_measurements,name='edit-measurements'),
    path('api/filter-customers/',views.filter_customers,name='filter-customers')
] 