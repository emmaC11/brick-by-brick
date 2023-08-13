from django.shortcuts import render
from django.views import generic
from cart.models import LegoSet


class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = LegoSet.objects.all()

