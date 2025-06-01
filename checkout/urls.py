from django.urls import path

from . import views, webhooks
from .views import cache_checkout_data

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path(
        "checkout_success/<order_number>/",
        views.checkout_success,
        name="checkout_success",
    ),
    path("cache_checkout_data/", cache_checkout_data, name="cache_checkout_data"),
    path("webhook/", webhooks.webhook, name="stripe_webhook"),
]
