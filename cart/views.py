from django.shortcuts import render, get_object_or_404    
from django.views import generic
from cart.models import LegoSet
from .utils import get_or_set_order_session


class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = LegoSet.objects.all()


class LegoSetDetailView(generic.FormView):
    template_name = 'cart/product.html'
    # queryset = LegoSet.objects.all()

    def get_object(self):
        return get_object_or_404(LegoSet, slug=self.kwargs['slug'])

