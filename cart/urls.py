from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart_summary'),
    path('shop/', views.ProductListView.as_view(), name='product_list'),
    path('shop/<slug>/', views.LegoSetDetailView.as_view(), name='product_detail'),
    path('increase_quantity/<pk>/', views.IncrementLegoSetQuantityView.as_view(), name='increase_quantity'),
    path('decrease_quantity/<pk>/', views.DecrementLegoSetQuantityView.as_view(), name='decrease_quantity'),
]
