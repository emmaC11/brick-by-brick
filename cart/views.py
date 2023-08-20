from django.conf import settings
from django.contrib import messages
from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404  
from django.views import generic
from .forms import AddToCartForm, AddressForm
from cart.models import LegoSet, OrderItem, Address
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
        return reverse("cart:cart_summary")
    
    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        legoset = self.get_object()

        item_filter = order.legoorderitems.filter(item=legoset)
        if item_filter.exists():
            item = item_filter.first()
            item.quantity += int(form.cleaned_data['quantity'])
            item.save()
        else:
            new_item = form.save(commit=False)
            new_item.item = legoset
            new_item.userOrder = order
            new_item.save()

        print('below is the order items count')
        print(order.legoorderitems.count())

        return super(LegoSetDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LegoSetDetailView, self).get_context_data(**kwargs)
        context['legoset'] = self.get_object()
        return context
    
    
# want to see items in our cart
class CartView(generic.TemplateView):
    template_name = 'cart/cart.html'
    
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context
        
    
class IncrementLegoSetQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        # increment LegoSet quantity & redirect to the cart
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.quantity += 1
        order_item.save()
        return redirect("cart:cart_summary")


class DecrementLegoSetQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        # increment LegoSet quantity & redirect to the cart
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])

        # delete order item object if quantity is less than or equal to one
        if order_item.quantity <= 1:
            order_item.delete()
        # decrement
        else:
            order_item.quantity -= 1
            order_item.save()
        return redirect("cart:cart_summary")


class RemoveLegoSetFromCartView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect("cart:cart_summary")


class CheckoutView(generic.FormView):
    template_name = 'cart/checkout.html'
    form_class = AddressForm

    def get_success_url(self):
        return reverse("cart:payment")

    def form_valid(self,form):
        order = get_or_set_order_session(self.request)
        selected_shipping_address = form.cleaned_data.get('selected_shipping_address')
        selected_billing_address = form.cleaned_data.get('selected_shipping_address')

        # use address from dropdown if selected or create new address using Address model
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


class OrderCompleteView(generic.TemplateView):
    template_name = 'cart/order_complete.html'
