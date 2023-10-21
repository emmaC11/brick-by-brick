from django.shortcuts import render
from django.views import generic
from cart.models import LegoSet
from django.urls import reverse


# CRUD FUNCTIONALITY

class CreateLegoSetView(generic.CreateView):
    template_name = 'manager/create_product.html'

    def get_success_url(self):
        return reverse("cart:product_list")


class UpdateLegoSetView(generic.UpdateView):
    print('add logic to update legoset')


class DeleteLegoSetView(generic.DeleteView):
    template_name = 'manager/delete_product.html'
    queryset = LegoSet.objects.all()

    def get_success_url(self):
        return reverse("cart:product_list")
