from django.urls import path
from lego_main import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
