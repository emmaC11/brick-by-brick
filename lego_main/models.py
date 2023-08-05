from django.db import models


class LegoSet(models.Model):
    pass


class LegoSetTheme(models.Model):
    pass


# when a lego set is added to the cart it becomes an order item
class OrderItem(models.Model):
    pass


class Order(models.Model):
    pass
