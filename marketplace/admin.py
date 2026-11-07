from django.contrib import admin
from .models import Car, Property, Cart, Enquiry, Favorite

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'year', 'transmission')
    search_fields = ('title', 'brand')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'location', 'price', 'bedrooms')
    search_fields = ('title', 'location', 'property_type')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('sender', 'car', 'property', 'date')

admin.site.register(Cart)
admin.site.register(Favorite)