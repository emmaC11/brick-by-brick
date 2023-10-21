from django.shortcuts import render
from django.views import generic
from cart.models import LegoSet
from django.urls import reverse


# CRUD FUNCTIONALITY

class CreateLegoSetView(generic.CreateView):
    print('add logic to create legoset')


class UpdateLegoSetView(generic.UpdateView):
    print('add logic to update legoset')


class DeleteLegoSetView(generic.DeleteView):
    template_name = 'manager/delete_product.html'
    queryset = LegoSet.objects.all()

    def get_success_url(self):
        return reverse("cart:product_list")
