from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, reverse
from django.views import generic
from cart.models import LegoSet, Order


class UserProfileView(generic.TemplateView):
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(
                user=self.request.user, ordered=True
                )
        })
        return context


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class MarketingFormView(generic.TemplateView):
    template_name = 'marketing.html'


def handler404(request, exception):
    """Error Handler 404 - Page Not Found"""
    return render(request, "errors/404.html", status=404)


def handler500(request, exception=None):
    """Error handler 500 - Server Error"""
    return render(request, "errors/500.html", status=500)
