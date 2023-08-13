from django.shortcuts import render
from django.views import generic
from cart.models import LegoSet


class ProductListView(generic.ListView):
    queryset = LegoSet.objects.all()

