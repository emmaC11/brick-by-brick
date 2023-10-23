from django.shortcuts import render
from django.views import generic
from cart.models import LegoSet
from django.urls import reverse
from manager.forms import LegoSetForm


# CRUD FUNCTIONALITY

class CreateLegoSetView(generic.CreateView):
    template_name = 'manager/create_product.html'
    form_class = LegoSetForm

    def get_success_url(self):
        return reverse("cart:product_list")

    def form_valid(self, form):
        form.save()
        return super(CreateLegoSetView, self).form_valid(form)


class UpdateLegoSetView(generic.UpdateView):
    template_name = 'manager/update_product.html'
    queryset = LegoSet.objects.all()
    form_class = LegoSetForm

    def get_success_url(self):
        return reverse("cart:product_list")

    def form_valid(self, form):
        form.save()
        return super(UpdateLegoSetView, self).form_valid(form)


class DeleteLegoSetView(generic.DeleteView):
    template_name = 'manager/delete_product.html'
    queryset = LegoSet.objects.all()

    def get_success_url(self):
        return reverse("cart:product_list")
