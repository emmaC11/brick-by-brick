from django.contrib import admin
from .models import LegoSetTheme, LegoSet, OrderItem, Order, Address, Payment


class AddressAdminDisplay(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'postal_code',
        'address_type',
    ]


admin.site.register(LegoSetTheme)
admin.site.register(LegoSet)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Address, AddressAdminDisplay)
admin.site.register(Payment)

# Register your models here.
