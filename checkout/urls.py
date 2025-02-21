from django.urls import path
from . import views
from checkout import webhooks 


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('webhook/', webhooks.webhook, name='stripe_webhook'),
]
