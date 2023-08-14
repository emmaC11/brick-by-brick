from django.shortcuts import render
from django.views import generic
from cart.models import LegoSet
from .utils import get_cart_items_and_total


class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = LegoSet.objects.all()


class LegoSetDetailView(generic.DetailView):
    template_name = 'cart/product.html'
    queryset = LegoSet.objects.all()

