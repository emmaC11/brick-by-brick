from django.urls import path, include
from lego_main import views
from .views import handler404

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('marketing/', views.MarketingFormView.as_view(), name='marketing'),
    path('cart/', include('cart.urls', namespace='cart')),
    path(
        'user_profile/',
        views.UserProfileView.as_view(),
        name='user_profile'),
]

handler404 = 'lego_main.views.handler404'
