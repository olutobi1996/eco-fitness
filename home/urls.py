from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.product_list, name='products'), 
     path('add/', views.add_product, name='add_product'), 
    path('plans/', views.plans, name='plans'),  
    path('reviews/', views.reviews, name='reviews'),  
    path('shop/', views.shop, name='shop'),  
    path('community/', views.community, name='community'),  
    path('contact/', views.contact, name='contact'),  
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
]
