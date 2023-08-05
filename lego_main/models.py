from django.db import models
from cloudinary.models import CloudinaryField


class LegoSetTheme(models.Model):
    theme_name = models.CharField(max_length=200)
    theme_description = models.CharField(max_length=500)

    def __str__(self):
        return self.theme_name


class LegoSet(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    piece_count = models.PositiveIntegerField()
    item_number = models.PositiveIntegerField()
    ages = models.PositiveIntegerField()
    minifigures = models.PositiveIntegerField()
    stock_quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    image = CloudinaryField('image', default='placeholder')
    theme = models.ForeignKey(LegoSetTheme, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    pass

# when a lego set is added to the cart it becomes an order item
class OrderItem(models.Model):
    pass


class Order(models.Model):
    pass
