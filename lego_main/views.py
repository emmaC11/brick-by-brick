from django.shortcuts import render
from django.views import generic
from .models import LegoSet

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'


def product_list(request):
    context = {
        'lego_sets': LegoSet.objects.all(),
    }
    return render(request, 'product_list.html')
