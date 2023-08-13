from django.urls import path
from lego_main import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product_list/', views.product_list, name='product_list'),
    path('marketing/', views.MarketingFormView.as_view(), name='marketing'),
    # path('cart/', include('cart.urls', namespace='cart')),

]
