from django.contrib import admin

from .models import LegoSetTheme, LegoSet, OrderItem, Order

# Register your models here.
admin.site.register(LegoSetTheme)
admin.site.register(LegoSet)
admin.site.register(OrderItem)
admin.site.register(Order)
