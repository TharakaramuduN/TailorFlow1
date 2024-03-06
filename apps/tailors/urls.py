from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.tailor_login,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='tailors/password_reset.html'),name='password_reset'),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name='tailors/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='tailors/set_password.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='tailors/password_reset_complete.html'), name='password_reset_complete'),
]