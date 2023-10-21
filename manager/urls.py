from django.urls import path
from manager import views

app_name = 'manager'

urlpatterns = [
    path('create/', views.CreateLegoSetView.as_view(), name='legoset-create'),
    path('delete/<pk>/', views.DeleteLegoSetView.as_view(),
         name='legoset_delete')
 
]
