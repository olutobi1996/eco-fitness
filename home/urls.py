from django.contrib import admin
from django.urls import path
from . import views
from products.views import shop_view 
from subscriptions.views import plans_view  


urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_product, name='add_product'), 
    path('plans/', plans_view, name='plans'),    
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
]
