"""
ViewModel for handling property marketplace business logic and data preparation.
Separates real estate filtering and data formatting from Django Views and Models.
"""
from marketplace.models import Property

class PropertyViewModel:
    @staticmethod
    def get_filtered_properties(property_type=None, max_price=None, location=None):
        properties = Property.objects.all()
        
        if property_type:
            properties = properties.filter(property_type__iexact=property_type)
        if max_price:
            properties = properties.filter(price__lte=max_price)
        if location:
            properties = properties.filter(location__icontains=location)
            
        return [{
            'id': prop.id,
            'title': prop.title,
            'type': prop.property_type,
            'price': prop.price,
            'location': prop.location,
            'image': prop.image.url if prop.image else None,
            'status': 'Available'
        } for prop in properties]