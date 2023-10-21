from django.urls import path
from manager import views

app_name = 'manager'

urlpatterns = [
    path('create/', views.CreateLegoSetView.as_view(), name='legoset_create'),
    path('update/<pk>/', views.UpdateLegoSetView.as_view(),
         name='legoset_update'),
    path('delete/<pk>/', views.DeleteLegoSetView.as_view(),
         name='legoset_delete')
]
