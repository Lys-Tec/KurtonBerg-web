from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('login/', views.custom_login_view, name='login'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='marketplace_home'),
    path('dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
]