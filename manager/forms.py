from django import forms
from cart.models import LegoSet


class LegoSetForm(forms.ModelForm):
    class Meta:
        model = LegoSet
        fields = ['name', 'slug', 'price', 'piece_count', 'item_number',
                  'ages', 'minifigures', 'stock_quantity', 'image', 'theme']
