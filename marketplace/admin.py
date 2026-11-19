from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import AdminProfile, Car, Property, Enquiry
from .models import Asset, Booking, BookingHistory, DfaState, DfaTransition

class AdminProfileInline(admin.StackedInline):
    model = AdminProfile
    can_delete = False
    verbose_name_plural = 'Admin Profile'
    fk_name = 'user'

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (AdminProfileInline,)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'created_at')
    search_fields = ('brand', 'model', 'title')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'location', 'price', 'bedrooms', 'bathrooms')
    search_fields = ('title', 'location', 'property_type')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'created_at')
    search_fields = ('subject', 'message', 'user__username')
    
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'title', 'price_per_month', 'status')
    search_fields = ('title', 'type')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset', 'customer_name', 'customer_nrc', 'current_state', 'updated_at')
    list_filter = ('current_state', 'created_at')
    search_fields = ('customer_name', 'customer_nrc')

@admin.register(BookingHistory)
class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ('booking', 'from_state', 'event', 'to_state', 'changed_at')
    list_filter = ('event', 'changed_at')

admin.site.register(DfaState)
admin.site.register(DfaTransition)    