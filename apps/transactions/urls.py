from django.urls import path
from . import views

urlpatterns = [
    path('transactions/',views.transactions,name='Transactions'),
    path('api/filter-transactions/',views.filter_transactions,name='filter-transactions')
]
