from django import forms


class MarketingForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Your email address'
    }))
