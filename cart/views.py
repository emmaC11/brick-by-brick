from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404  
from django.views import generic
from cart.models import LegoSet
from .utils import get_or_set_order_session
from django.urls import reverse


class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = LegoSet.objects.all()


class LegoSetDetailView(generic.FormView):
    template_name = 'cart/product.html'
    # queryset = LegoSet.objects.all()

    def get_object(self):
        return get_object_or_404(LegoSet, slug=self.kwargs['slug'])
    
    def get_success_url(self):
        return reverse("home")
    
    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        legoSet = self.get_object()

        return super(LegoSetDetailView, self).form_valid(form)

