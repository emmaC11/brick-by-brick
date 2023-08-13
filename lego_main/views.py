from django.shortcuts import render
from django.views import generic
from .models import LegoSet
from .forms import MarketingForm

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class MarketingFormView(generic.FormView):
    template_name = 'marketing.html'
    form_class = MarketingForm

    def get_success_url(self):
        return reverse("marketing")
    
    def form_valid(self, form):
        messages.info(self.request, "You are now subscribed!")
        return super(MarketingFormView).form_valid(form)
        


def product_list(request):
    context = {
        'lego_sets': LegoSet.objects.all(),
    }
    return render(request, 'product_list.html')
