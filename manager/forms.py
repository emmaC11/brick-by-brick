from django import forms
from cart.models import LegoSet


class LegoSetForm(forms.ModelForm):
    class Meta:
        model = LegoSet
        fields = ['name', 'price', 'piece_count', 'ages', 'minifigures',
                  'stock_quantity', 'image', 'theme']
