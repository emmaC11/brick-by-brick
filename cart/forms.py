from typing import Any, Dict
from django.contrib.auth import get_user_model
from django import forms
from cart.models import OrderItem, Address


User = get_user_model()


class AddToCartForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['quantity']


class AddressForm(forms.Form):
    # defining shipping & billing address within same form
    shipping_address_line_1 = forms.CharField(required=False)
    shipping_address_line_2 = forms.CharField(required=False)
    shipping_city = forms.CharField(required=False)
    shipping_postal_code = forms.CharField(required=False)

    billing_address_line_1 = forms.CharField(required=False)
    billing_address_line_2 = forms.CharField(required=False)
    billing_city = forms.CharField(required=False)
    billing_postal_code = forms.CharField(required=False)

    # storing the selected shipping & billing address from Address model
    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )
    selected_billing_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)

        user = User.objects.get(id=user_id)

        shipping_address_qs = Address.objects.filter(
            user=user,
            address_type='S'
        )

        billing_address_qs = Address.objects.filter(
            user=user,
            address_type='B'
        )

        self.fields['selected_shipping_address'].queryset = shipping_address_qs
        self.fields['selected_billing_address'].queryset = billing_address_qs

    # if shipping or billing address is selected, then the other address is not required
    def clean(self):
        data = self.cleaned_data

        selected_shipping_address = data.get('selected_shipping_address', None)
        if selected_shipping_address is None:
            if not data.get('shipping_address_line_1', None):
                self.add_error('shipping_address_line_1', 'Please fill in this field')
            if not data.get('shipping_address_line_2', None):
                self.add_error('shipping_address_line_2', 'Please fill in this field')
            if not data.get('shipping_city', None):
                self.add_error('shipping_city', 'Please fill in this field')
            if not data.get('shipping_postal_code', None):
                self.add_error('shipping_postal_code', 'Please fill in this field')