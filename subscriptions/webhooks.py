
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import stripe
from django.conf import settings
from .webhook_handler import StripeWH_Handler

@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""

    # Get Stripe webhook secret and API key from settings
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Retrieve the webhook payload and signature header
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', None)
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    # Initialize the webhook handler
    handler = StripeWH_Handler(request)

    # Map Stripe events to their handlers
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
        # Add other events here as needed
    }

    # Get the event type from Stripe
    event_type = event['type']

    # Get the handler function for the event type, or use the generic one
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the handler with the event
    return event_handler(event)

