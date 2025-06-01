from django.urls import path

from .views import create_checkout_session, plans_view, subscription_success
from .webhooks import webhook

urlpatterns = [
    path(
        "checkout/<str:price_id>/",
        create_checkout_session,
        name="subscriptions-checkout",
    ),
    path("webhook/", webhook, name="stripe_webhook"),  # Use 'webhook' here
    path("plans/", plans_view, name="plans"),
    path("success/", subscription_success, name="subscription_success"),
]
