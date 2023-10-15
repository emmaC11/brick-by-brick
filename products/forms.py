from django import forms
from products.models import LegoSetTheme


class LegoThemeFilterForm(forms.Form):
    theme_choices = [
        (theme.id, theme.theme_name) for theme in LegoSetTheme.objects.all()]
    selected_theme = forms.ChoiceField(choices=[
        ('', 'All Themes')] + theme_choices, required=False)
