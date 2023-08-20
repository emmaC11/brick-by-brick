from django import forms
from cart.models import OrderItem, Address


class AddToCartForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['quantity']


class AddressForm(forms.Form):
    # defining shipping & billing address within same form
    shipping_address_line_1 = forms.CharField()
    shipping_address_line_2 = forms.CharField()
    shipping_city = forms.CharField()
    shipping_postal_code = forms.CharField()

    billing_address_line_1 = forms.CharField()
    billing_address_line_2 = forms.CharField()
    billing_city = forms.CharField()
    billing_postal_code = forms.CharField()

    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )
    

    
