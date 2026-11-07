from .forms import EnquiryForm
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Car, Property
from django.contrib.auth.decorators import login_required
from .models import Favorite
from django.shortcuts import render, get_object_or_404

from .models import Car, Property
from .forms import EnquiryForm

def home(request):
    cars = Car.objects.filter(approved=True, available=True)
    properties = Property.objects.filter(approved=True, available=True)

    # Filters
    brand = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    location = request.GET.get('location')

    if brand:
        cars = cars.filter(brand__icontains=brand)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)
    if location:
        properties = properties.filter(location__icontains=location)

    form = EnquiryForm()

    # FORM SUBMISSION
    if request.method == 'POST' and request.user.is_authenticated:
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)

            car_id = request.POST.get('car_id')
            property_id = request.POST.get('property_id')

            if car_id:
                enquiry.car_id = car_id
            if property_id:
                enquiry.property_id = property_id

            enquiry.sender = request.user
            enquiry.save()
            return redirect('home')

    context = {
        'cars': cars,
        'properties': properties,
        'form': form,
    }
    return render(request, 'marketplace/home.html', context)


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = EnquiryForm()

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            enquiry = form.save(commit=False)
            enquiry.sender = request.user
            enquiry.car = car
            enquiry.save()
            return redirect('car_detail', pk=car.pk)

    return render(request, 'marketplace/car_detail.html', {'car': car, 'form': form})


def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    form = EnquiryForm()

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            enquiry = form.save(commit=False)
            enquiry.sender = request.user
            enquiry.car = None
            enquiry.save()
            return redirect('property_detail', pk=property.pk)

    return render(request, 'marketplace/property_detail.html', {'property': property, 'form': form})


@login_required
def add_favorite_car(request, car_id):
    car = Car.objects.get(id=car_id)
    Favorite.objects.get_or_create(user=request.user, car=car)
    return redirect('home')


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id, approved=True, available=True)
    return render(request, 'marketplace/car_detail.html', {'car': car})

def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id, approved=True, available=True)
    return render(request, 'marketplace/property_detail.html', {'property': property})

def home(request):
    cars = Car.objects.filter(approved=True, available=True)
    properties = Property.objects.filter(approved=True, available=True)

    context = {'cars': cars, 'properties': properties}
    return render(request, 'marketplace/home.html', context)
