"""
Marketplace views utilizing the MVVM architecture.
Delegates business logic and data formatting to ViewModels.
"""
from django.shortcuts import render, get_object_or_404
from marketplace.models import Car, Property
from marketplace.viewmodels.car_viewmodel import CarViewModel
from marketplace.viewmodels.property_viewmodel import PropertyViewModel

def home_view(request):
    # Extract GET query parameters for filtering
    car_brand = request.GET.get('car_brand')
    car_max_price = request.GET.get('car_max_price')
    
    prop_type = request.GET.get('prop_type')
    prop_max_price = request.GET.get('prop_max_price')
    prop_location = request.GET.get('prop_location')

    context = {
        'cars': CarViewModel.get_filtered_cars(brand=car_brand, max_price=car_max_price),
        'properties': PropertyViewModel.get_filtered_properties(
            property_type=prop_type, 
            max_price=prop_max_price, 
            location=prop_location
        ),
    }
    return render(request, 'marketplace/home.html', context)

def car_detail_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'marketplace/car_detail.html', {'car': car})

def property_detail_view(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    return render(request, 'marketplace/property_detail.html', {'property': property_obj})