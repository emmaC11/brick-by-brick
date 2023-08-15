from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404  
from django.views import generic
from .forms import AddToCartForm
from cart.models import LegoSet
from .utils import get_or_set_order_session
from django.urls import reverse


class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = LegoSet.objects.all()


class LegoSetDetailView(generic.FormView):
    template_name = 'cart/product.html'
    form_class = AddToCartForm
    # queryset = LegoSet.objects.all()

    def get_object(self):
        return get_object_or_404(LegoSet, slug=self.kwargs["slug"])
    
    def get_success_url(self):
        return reverse("home")
    
    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        legoset = self.get_object()

        item_filter = order.items.filter(item=legoset)
        if item_filter.exists():
            item = item_filter.first()
            item.quantity += int(form.cleaned_data['quantity'])
            item.save()
        else:
            new_item = form.save(commit=False)
            new_item.item = legoset
            new_item.userOrder = order
            new_item.save()

        return super(LegoSetDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LegoSetDetailView, self).get_context_data(**kwargs)
        context['legoset'] = self.get_object()
        return context
    
    
# want to see items in our cart
class CartView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context["userOrder"] = get_or_set_order_session(self.request)
        
    
    
