from django.urls import path
from .views import create_checkout_session, plans_view  
from .webhooks import stripe_webhook  

urlpatterns = [
    path('checkout/<str:price_id>/', create_checkout_session, name='checkout'),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
    path('plans/', plans_view, name='plans'),
]

