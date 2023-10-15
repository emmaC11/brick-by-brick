from django.db import models
from django.contrib.auth.models import User


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
