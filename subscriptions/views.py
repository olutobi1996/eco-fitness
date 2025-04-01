from django.shortcuts import render
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def create_checkout_session(request, price_id):
    """Creates a Stripe checkout session for subscription"""
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='subscription',  # This enables subscription mode
        customer_email=request.user.email,  
        line_items=[{
            'price': price_id,  # Stripe price ID from your Stripe product
            'quantity': 1,
        }],
        success_url=request.build_absolute_uri(reverse('subscription_success')),
        cancel_url=request.build_absolute_uri(reverse('subscription_cancel')),
    )
    return redirect(checkout_session.url)

def plans_view(request):
    return render(request, 'subscriptions/plans.html')  

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import stripe

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
