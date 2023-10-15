from django.shortcuts import render
from django.views import generic
from products.models import LegoSet, LegoSetTheme
from products.forms import LegoThemeFilterForm


class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = LegoSet.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        theme_id = self.request.GET.get('selected_theme')
        if theme_id:
            queryset = queryset.filter(theme=theme_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lego_theme_filter_form'] = LegoThemeFilterForm()

        # get selected theme's description and pass it to the context
        selected_theme_id = self.request.GET.get('selected_theme')
        if selected_theme_id:
            selected_theme = LegoSetTheme.objects.get(pk=selected_theme_id)
            context['selected_theme_description'] = (
                selected_theme.theme_description
            )
            context['selected_theme_name'] = selected_theme.theme_name
        return context
