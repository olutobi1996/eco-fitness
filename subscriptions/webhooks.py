import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Subscription

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    """Handles Stripe subscription webhooks"""
    payload = request.body
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Handle subscription events
    if event['type'] == 'customer.subscription.updated':
        subscription_data = event['data']['object']
        stripe_subscription_id = subscription_data['id']
        status = subscription_data['status']

        # Update subscription in the database
        try:
            subscription = Subscription.objects.get(stripe_subscription_id=stripe_subscription_id)
            subscription.status = status
            subscription.save()
        except Subscription.DoesNotExist:
            pass  # Subscription not found (possibly a new one)

    return JsonResponse({'status': 'success'})
