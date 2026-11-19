from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    profile_picture = models.FileField(upload_to='admin_profiles/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class Car(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2, help_text="Price in ZMW")
    mileage = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars_listed', blank=True, null=True)
    seller_name = models.CharField(max_length=255, blank=True, null=True, help_text="Displayed seller/consignor name")
    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ZMW {self.price}"

class Property(models.Model):
    title = models.CharField(max_length=200)
    property_type = models.CharField(max_length=100, help_text="e.g. House, Commercial, Land, Villa")
    location = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=14, 
                                decimal_places=2, help_text="Price in ZMW")
    bedrooms = models.PositiveIntegerField(blank=True, null=True)
    bathrooms = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties_listed', blank=True, null=True)
    seller_name = models.CharField(max_length=255, blank=True, null=True, help_text="Displayed seller/consignor name")
    is_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.location}) - ZMW {self.price}"
class Enquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enquiries')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry by {self.user.username} on {self.subject}"

class SellerApplication(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_application')
    business_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    id_number_or_pacra = models.CharField(max_length=100, blank=True, null=True, help_text="NRC or PACRA Registration Number")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.business_name or 'Unspecified'} ({self.status})"                  
class DfaState(models.Model):
    state_code = models.CharField(max_length=50, primary_key=True)
    is_accepting = models.BooleanField(default=False)
    is_start = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dfa_states'

    def __str__(self):
        return self.state_code

class DfaTransition(models.Model):
    from_state = models.ForeignKey(DfaState, models.DO_NOTHING, db_column='from_state', related_name='transitions_from')
    event = models.CharField(max_length=255)
    to_state = models.ForeignKey(DfaState, models.DO_NOTHING, db_column='to_state', related_name='transitions_to')

    class Meta:
        managed = False
        db_table = 'dfa_transitions'
        unique_together = (('from_state', 'event'),)

class Asset(models.Model):
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    price_per_month = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, default='AVAILABLE')

    class Meta:
        managed = False
        db_table = 'assets'

    def __str__(self):
        return f"{self.type}: {self.title}"

class Booking(models.Model):
    asset = models.ForeignKey(Asset, models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_nrc = models.CharField(max_length=50, blank=True, null=True)
    current_state = models.CharField(max_length=50, default='REQUESTED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bookings'

    def __str__(self):
        return f"Booking #{self.id} - {self.customer_name} ({self.current_state})"

class BookingHistory(models.Model):
    booking = models.ForeignKey(Booking, models.CASCADE)
    from_state = models.CharField(max_length=50, blank=True, null=True)
    event = models.CharField(max_length=50, blank=True, null=True)
    to_state = models.CharField(max_length=50, blank=True, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'booking_history'