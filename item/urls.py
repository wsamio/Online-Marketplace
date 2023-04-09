from django.urls import path
from . import views

urlpatterns = [
    path('', views.allItems, name='all-items'),
    path('item/<str:pk>/', views.singleItem, name='single-item'), 
    path('create-item/', views.createItem, name='create-item'),  
]