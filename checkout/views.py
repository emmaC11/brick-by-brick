import datetime
import json
from django.shortcuts import render
from django.views import generic
from cart.utils import get_or_set_order_session
from user_details.models import Address
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from checkout.models import Payment
from django.http import JsonResponse
from user_details import AddressForm


class CheckoutView(generic.FormView):
    template_name = 'cart/checkout.html'
    form_class = AddressForm

    def get_success_url(self):
        return reverse("cart:payment")

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        selected_shipping_address = form.cleaned_data.get(
            'selected_shipping_address'
            )
        selected_billing_address = form.cleaned_data.get(
            'selected_shipping_address'
            )

        # use address from dropdown if selected
        # or create new address using Address model
        if selected_shipping_address:
            order.shipping_address = selected_shipping_address
        else:
            address = Address.objects.create(
                address_type='S',
                user=self.request.user,
                address_line_1=form.cleaned_data['shipping_address_line_1'],
                address_line_2=form.cleaned_data['shipping_address_line_2'],
                city=form.cleaned_data['shipping_city'],
                postal_code=form.cleaned_data['shipping_postal_code'],
            )
            order.shipping_address = address

        if selected_billing_address:
            order.billing_address = selected_billing_address
        else:
            address = Address.objects.create(
                address_type='B',
                user=self.request.user,
                address_line_1=form.cleaned_data['billing_address_line_1'],
                address_line_2=form.cleaned_data['billing_address_line_2'],
                city=form.cleaned_data['billing_city'],
                postal_code=form.cleaned_data['billing_postal_code'],
            )
            order.billing_address = address

        order.save()
        messages.info(
            self.request, "Thank you! You have added your address details.")
        return super(CheckoutView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CheckoutView, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context


class PaymentView(generic.TemplateView):
    template_name = 'cart/payment.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        context["PAYPAL_CLIENT_ID"] = settings.PAYPAL_CLIENT_ID
        context['order'] = get_or_set_order_session(self.request)
        return context


class OrderConfirmedView(generic.View):
    def post(self, request, *args, **kwargs):
        order = get_or_set_order_session(self.request)
        body = json.loads(request.body)
        # temp print statements to see what is being sent to the server

        # want to save this data to our order model
        print(body)
        payment = Payment.objects.create(
            order=order,
            payment_successful=True,
            raw_response=json.dumps(body),
            amount=float(body['purchase_units'][0]['amount']['value']),
            payment_method='PayPal',
        )
        order.ordered = True
        order.order_date = datetime.date.today()
        order.save()
        return JsonResponse({"data": "OK"})


class OrderCompleteView(generic.TemplateView):
    template_name = 'cart/order_complete.html'
