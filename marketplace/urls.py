from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('home/', views.home_view, name='home'),
    path('home/', views.home_view, name='marketplace_home'),
    path('login/', views.custom_login_view, name='login'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('apply-seller/', views.apply_seller_view, name='apply_seller'),
    path('cars/<int:pk>/', views.car_detail_view, name='car_detail'),
    path('properties/<int:pk>/', views.property_detail_view, name='property_detail'),
    path('add-car/', views.add_car_view, name='add_car'),
    path('add-property/', views.add_property_view, name='add_property'),
]