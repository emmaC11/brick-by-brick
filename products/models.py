from django.db import models
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField


class LegoSetTheme(models.Model):
    theme_name = models.CharField(max_length=200)
    theme_description = models.CharField(max_length=500)

    def __str__(self):
        return self.theme_name


class LegoSet(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    price = models.IntegerField(default=0)
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

    def get_legoset(self):
        return reverse('cart:product_detail', args=[self.slug])

    def get_legoset_price(self):
        # divide by 100 to get the price in euro/chosen currency
        return "{:.2f}".format(self.price/100)