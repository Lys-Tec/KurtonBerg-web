
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
# ------------------------
# 1. Car model
# ------------------------
class Car(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)  # who is selling
    title = models.CharField(max_length=200)                   # car name
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    transmission = models.CharField(max_length=50)             # Auto/Manual
    fuel_type = models.CharField(max_length=50)               # Petrol/Diesel/Electric
    description = models.TextField()
    available = models.BooleanField(default=True)             # is the car available?
    approved = models.BooleanField(default=False)             # admin approval
    image = models.FileField(upload_to='cars/', blank=True, null=True)
    def __str__(self):
        return self.title

# ------------------------
# 2. Cart model
# ------------------------
class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


# ------------------------
# 4. Property model (Real Estate)
# ------------------------
class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    property_type = models.CharField(max_length=100)  # House, Plot, Apartment
    location = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    image = models.FileField(upload_to='properties/', blank=True, null=True)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title

# ------------------------
# 3. Enquiry model
# ------------------------
class Enquiry(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        if self.car:
            return f"Enquiry for Car: {self.car.title}"
        if self.property:
            return f"Enquiry for Property: {self.property.title}"
        return "General Enquiry"
    
    #-----------------------
    #    4 Favorite model
    #-----------------------
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} favorite"



class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('BUYER', 'Buyer'),
        ('SELLER', 'Seller'),
        ('ADMIN', 'Super Admin'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='BUYER')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_verified_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"


class SellerApplication(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_applications')
    business_name = models.CharField(max_length=255)
    nrc_number = models.CharField(max_length=50, help_text="National Registration Card or Passport Number")
    phone_number = models.CharField(max_length=20)
    business_address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    admin_notes = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.business_name} ({self.user.username}) - {self.status}"