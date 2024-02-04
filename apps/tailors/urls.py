from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.Tailorlogin,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile')
]