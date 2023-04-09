from django.urls import path
from . import views

urlpatterns = [
    path('', views.allItems, name='all-items'),
    path('item/<str:pk>/', views.singleItem, name='single-item'), 
    path('create-item/', views.createItem, name='create-item'),
    path('delete-item/<str:pk>', views.deleteItem, name='delete-item'),
    path('edit-item/<str:pk>', views.editItem, name='edit-item'),
    path('browse/', views.browseItem, name='browse'),
]