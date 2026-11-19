from django import forms
from .models import Enquiry
from .models import Car, Property
from django.db import models
from django.contrib.auth.models import User
from .models import SellerApplication

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'brand', 'model', 'year', 'price', 'mileage', 'image', 'seller_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2021 Toyota Land Cruiser V8'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Toyota'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Land Cruiser'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2021'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price in ZMW'}),
            'mileage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Automatic • Diesel • 45,000 km'}),
            'seller_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KurtonBerg Agency Direct'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'property_type', 'location', 'price', 'bedrooms', 'image', 'seller_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 5 Bed Executive Villa'}),
            'property_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Villa, House, Land'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sunningdale, Lusaka'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price in ZMW'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '5'}),
            'seller_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KurtonBerg Agency Direct'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Ask about this item...'
            })
        }

    

class SellerApplicationForm(forms.ModelForm):
    class Meta:
        model = SellerApplication
        fields = ['business_name', 'phone_number', 'id_number_or_pacra']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your business or legal name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. +260970000000'}),
            'id_number_or_pacra': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NRC or PACRA Registration Number'}),
        }    
        
        from django import forms
from .models import Car, Property

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'brand', 'model', 'year', 'price', 'mileage', 'image', 'seller_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2021 Toyota Land Cruiser V8'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Toyota'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Land Cruiser'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2021'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price in ZMW'}),
            'mileage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Automatic • Diesel • 45,000 km'}),
            'seller_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KurtonBerg Agency Direct'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'property_type', 'location', 'price', 'bedrooms', 'image', 'seller_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 5 Bed Executive Villa'}),
            'property_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Villa, House, Land'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sunningdale, Lusaka'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price in ZMW'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '5'}),
            'seller_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KurtonBerg Agency Direct'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }