from django.shortcuts import render
from django.views import generic
from cart.models import LegoSet


# CRUD FUNCTIONALITY

class CreateLegoSetView(generic.CreateView):
    print('add logic to create legoset')


class UpdateLegoSetView(generic.UpdateView):
    print('add logic to update legoset')


class DeleteLegoSetView(generic.DeleteView):
    queryset = LegoSet.objects.all
