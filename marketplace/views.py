from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car, Property, SellerApplication, UserProfile

def welcome_view(request):
    """Unified landing page featuring top assets and search bar"""
    recent_properties = Property.objects.all().order_by('-id')[:4]
    recent_cars = Car.objects.all().order_by('-id')[:4]

    context = {
        'recent_properties': recent_properties,
        'recent_cars': recent_cars,
    }
    return render(request, 'marketplace/welcome.html', context)

def home_view(request):
    """Catalog and search view for properties and cars"""
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    location = request.GET.get('location', '')

    properties = Property.objects.all()
    cars = Car.objects.all()

    if query:
        properties = properties.filter(title__icontains=query)
        cars = cars.filter(title__icontains=query)

    if location:
        properties = properties.filter(location__icontains=location)

    context = {
        'properties': properties,
        'cars': cars,
        'query': query,
        'category': category,
        'location': location,
    }
    return render(request, 'marketplace/home.html', context)

@login_required
def buyer_dashboard(request):
    """User dashboard for registered buyers and sellers"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'marketplace/buyer_dashboard.html', context)

def car_detail_view(request, pk):
    """Detailed view for a specific car listing"""
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'marketplace/car_detail.html', {'car': car})

def property_detail_view(request, pk):
    """Detailed view for a specific property listing"""
    property_item = get_object_or_404(Property, pk=pk)
    return render(request, 'marketplace/property_detail.html', {'property': property_item})

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_control_dashboard(request):
    """Secure custom admin command dashboard"""
    total_properties = Property.objects.count()
    total_cars = Car.objects.count()
    pending_applications = SellerApplication.objects.filter(is_approved=False)[:5]
    
    context = {
        'total_properties': total_properties,
        'total_cars': total_cars,
        'pending_applications': pending_applications,
    }
    return render(request, 'marketplace/admin_dashboard.html', context)

import random
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            otp = str(random.randint(100000, 999999))
            request.session['pre_auth_user_id'] = user.id
            request.session['login_otp'] = otp
            
            send_mail(
                'Your KurtonBerg Agency Login OTP',
                f'Your verification code is: {otp}',
                'noreply@kurtonberg.com',
                [user.email],
                fail_silently=True,
            )
            print(f"DEBUG OTP for {user.username}: {otp}")
            return redirect('verify_otp')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'marketplace/login.html')

def verify_otp_view(request):
    if 'pre_auth_user_id' not in request.session:
        return redirect('login')
        
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('login_otp')
        
        if entered_otp == stored_otp:
            user_id = request.session.pop('pre_auth_user_id')
            request.session.pop('login_otp', None)
            
            user = User.objects.get(id=user_id)
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            return redirect('marketplace_home')
        else:
            messages.error(request, 'Invalid OTP code. Please try again.')
            
    return render(request, 'marketplace/verify_otp.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
            
    return render(request, 'marketplace/signup.html')