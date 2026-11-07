from django.urls import path
from marketplace import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('car/<int:pk>/', views.car_detail_view, name='car_detail'),
    path('property/<int:pk>/', views.property_detail_view, name='property_detail'),
]