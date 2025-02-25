"""
eco_fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin Panel
    path('accounts/', include('allauth.urls')),  # User Authentication
    path('', include('home.urls')),  # Home App
    path('bag/', include('bag.urls')),  # Shopping Bag
    path('products/', include('products.urls')),  # Product Pages
    path('checkout/', include('checkout.urls')),  # Checkout App
] 

