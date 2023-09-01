from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, reverse
from django.views import generic
from cart.models import LegoSet, Order
from .forms import MarketingForm


# Create your views here.
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


class MarketingFormView(generic.FormView):
    template_name = 'marketing.html'
    form_class = MarketingForm

    def get_success_url(self):
        return reverse("marketing")

    def form_valid(self, form):
        messages.info(self.request, "You are now subscribed!")
        email = form.cleaned_data.get("email")

        form_data = "Add user to marketing email list: {email}".format(
            email=email
            )

        send_mail(
            subject="New marketing email subscriber!",
            message=form_data,
            # from_email=settings.EMAIL_HOST_USER,
            # recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(MarketingFormView, self).form_valid(form)
