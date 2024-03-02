from django.urls import path
from . import views

urlpatterns = [
    path('create-product',views.create_product,name='create-product'),
    path('products/',views.products,name='products'),
    path('filter-products/',views.filter_products,name='filter-products')
]
