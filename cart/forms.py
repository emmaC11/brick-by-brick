from django import forms
from cart.models import OrderItem, Address


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

    selected_shipping_address = forms.ModelChoiceField(
        Address.objects.none(), required=False
    )
    

    
