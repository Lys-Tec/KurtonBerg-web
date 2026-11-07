"""
ViewModel for handling car marketplace business logic and data preparation.
Separates data processing from Django Views and Models.
"""
from marketplace.models import Car

class CarViewModel:
    @staticmethod
    def get_filtered_cars(brand=None, max_price=None):
        cars = Car.objects.all()
        if brand:
            cars = cars.filter(brand__icontains=brand)
        if max_price:
            cars = cars.filter(price__lte=max_price)
        
        return [{
            'id': car.id,
            'title': f"{car.brand} {car.model}",
            'price': car.price,
            'image': car.image.url if car.image else None,
            'status': 'Available'
        } for car in cars]