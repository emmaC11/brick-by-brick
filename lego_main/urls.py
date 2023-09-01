from django.urls import path, include
from lego_main import views
from django.views.defaults import page_not_found

urlpatterns = [
    path(
        '404/',
        page_not_found,
        {'exception': Exception('Page not Found')}, name='404'),
    path('', views.HomeView.as_view(), name='home'),
    path('marketing/', views.MarketingFormView.as_view(), name='marketing'),
    path('cart/', include('cart.urls', namespace='cart')),
    path(
        'user_profile/',
        views.UserProfileView.as_view(),
        name='user_profile'),
]
