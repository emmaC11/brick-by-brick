from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class LegoSetTheme(models.Model):
    theme_name = models.CharField(max_length=200)
    theme_description = models.CharField(max_length=500)

    def __str__(self):
        return self.theme_name


class LegoSet(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
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
    # specify the order item that is associated with a user & a order
    userOrder = models.ForeignKey("Order", related_name="legoorderitems", on_delete=models.CASCADE)

    item = models.ForeignKey(LegoSet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.item.name


class Order(models.Model):
    # associate order with a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    pass
