from django.urls import path
from . import views

urlpatterns = [
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
path('property/<int:pk>/', views.property_detail, name='property_detail'),
path('favorite/car/<int:pk>/', views.add_favorite_car, name='add_favorite_car'),
]
