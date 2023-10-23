from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField


class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)

    def __str__(self):
        return self.address_line_1

    class Meta:
        verbose_name_plural = 'Addresses'


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


# when a lego set is added to the cart it becomes an order item
class OrderItem(models.Model):
    # specify the order item that is associated with a user & a order
    userOrder = models.ForeignKey(
        "Order",
        related_name="legoorderitems",
        on_delete=models.CASCADE)

    item = models.ForeignKey(LegoSet, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"

    def get_raw_legoset_total(self):
        return self.quantity * self.item.price

    def get_legoset_total(self):
        price = self.get_raw_legoset_total()
        return "{:.2f}".format(price/100)


class Order(models.Model):
    # associate order with a user
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    # order is linked to an address
    billing_address = models.ForeignKey(
        Address,
        related_name="billing_address",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(
        Address,
        related_name="shipping_address",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.reference_number
    pass

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"

    def get_order_raw_subtotal(self):
        total = 0
        # append variable total with the total of each order item
        for order_item in self.legoorderitems.all():
            total += order_item.get_raw_legoset_total()
        return total

    def get_order_subtotal(self):
        subtotal = self.get_order_raw_subtotal()
        return "{:.2f}".format(subtotal/100)

    def get_order_raw_total(self):
        subtotal = self.get_order_raw_subtotal()
        # add default 5 euro shipping costs
        shipping_costs = 500
        return subtotal + shipping_costs

    def get_order_total(self):
        total = self.get_order_raw_total()
        return "{:.2f}".format(total/100)


class Payment(models.Model):
    # payment is linked to an order
    order = models.ForeignKey(
        Order, related_name='payments', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=(
        ('PayPal', 'PayPal'),
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_successful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return self.order

    @property
    def reference_number(self):
        return f"PAYMENT-{self.order}-{self.pk}"
