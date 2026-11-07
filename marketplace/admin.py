from django.contrib import admin
from .models import Car, Property, Cart, Enquiry, Favorite

from django.contrib import admin
from .models import UserProfile, SellerApplication
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


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'is_verified_seller', 'created_at')
    list_filter = ('role', 'is_verified_seller')
    search_fields = ('user__username', 'user__email', 'phone_number')

@admin.register(SellerApplication)
class SellerApplicationAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user', 'nrc_number', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('business_name', 'user__username', 'nrc_number', 'phone_number')
    actions = ['approve_applications', 'reject_applications']

    @admin.action(description='Approve selected seller applications')
    def approve_applications(self, request, queryset):
        for app in queryset:
            app.status = 'APPROVED'
            app.save()
            # Update user profile
            profile, created = UserProfile.objects.get_or_create(user=app.user)
            profile.role = 'SELLER'
            profile.is_verified_seller = True
            profile.save()
        self.message_user(request, "Selected applications have been approved.")

    @admin.action(description='Reject selected seller applications')
    def reject_applications(self, request, queryset):
        queryset.update(status='REJECTED')
        self.message_user(request, "Selected applications have been rejected.")