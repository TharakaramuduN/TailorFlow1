from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('update-status/<int:item_id>/<slug:status>/',views.update_status,name='update-status'),
    path('filter-products/',views.filter_products,name='filter-products')
]
