from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllCategor , name='allcategor'),
    path('home/', views.AllProduct , name='allproduct'),
    path('home/<slug:category>', views.BYcategory , name='bycategory'),
    path('home/edit/<int:pk>', views.EditProduct , name='edit'),
    path('home/delete/<int:pk>', views.DeleteProduct , name='delete'),
    path('create/', views.CreateProducts, name = 'crt'),
    path('home/add/<int:pk>', views.Add , name='add_cart'),
    path('savat/', views.Savat, name='savat'),
    path('savat/<int:pk>', views.ItemDelete, name='itemdelete'),
    path('search/', views.Search, name='search'),
]