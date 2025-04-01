from django.urls import path
from .views import create_checkout_session
from .webhooks import stripe_webhook
from .views import plans_view  

urlpatterns = [
    path('checkout/<str:plan>/', create_checkout_session, name='checkout'),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
    path('plans/', plans_view, name='plans'),
]
