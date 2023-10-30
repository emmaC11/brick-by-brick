from django.urls import path, include
from lego_main import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('cart/', include('cart.urls', namespace='cart')),
    path(
        'user_profile/',
        views.UserProfileView.as_view(),
        name='user_profile'),
]
