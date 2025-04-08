"""
eco_fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contact.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin Panel
    path('', include('home.urls')),  # Home App
    path('bag/', include('bag.urls')),  # Shopping Bag
    path('products/', include('products.urls', namespace="products")),  # Products (with namespace)
    path('checkout/', include('checkout.urls')), # Checkout App
    path("community/", include("community.urls")),  # Community Page
    path('subscriptions/', include('subscriptions.urls')),
    path('profile/', include('accounts.urls')),
    path('contact/', include('contact.urls')), 
    path('about-us/', include('about_us.urls')),
    path('accounts/', include('allauth.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




