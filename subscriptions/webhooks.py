import stripe
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.DJSTRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return JsonResponse({"error": "Invalid payload"}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({"error": "Invalid signature"}, status=400)

    # Handle subscription events
    if event["type"] == "invoice.payment_succeeded":
        print("Subscription payment received!")
    elif event["type"] == "customer.subscription.deleted":
        print("Subscription canceled!")

    return JsonResponse({"status": "success"})

