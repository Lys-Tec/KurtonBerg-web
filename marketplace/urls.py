from django.urls import path
from marketplace import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('home/', views.home_view, name='home'),
    path('home/', views.home_view, name='marketplace_home'),
    path('dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('car/<int:pk>/', views.car_detail_view, name='car_detail'),
    path('property/<int:pk>/', views.property_detail_view, name='property_detail'),
]