from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Subscription
from django.contrib.auth.decorators import login_required

# Load Stripe API keys
stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_checkout_session(request, price_id):
    try:
        # Setup the domain for success/cancel URLs
        domain_url = "https://eco-fitness-2b6c5d715c47.herokuapp.com"
        success_url = domain_url + reverse('subscription_success')  # Success URL after payment
        cancel_url = domain_url + "/subscriptions/cancel/"  # URL if the user cancels the checkout

        # Create Stripe checkout session for subscription
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url=success_url,  # The URL where the user is redirected after successful payment
            cancel_url=cancel_url,  # The URL where the user is redirected after canceling
        )

        return redirect(checkout_session.url)  # Redirect the user to Stripe Checkout

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def subscription_success(request):
    """
    Handle the successful subscription redirect.
    This function will be called after a successful payment session.
    """
    # You can add any logic to update the user's subscription status in your database here
    messages.success(request, "Your subscription was successful!")
    
    return render(request, "subscriptions/subscription_success.html", {
        "is_subscription": True,
    })


def subscription_cancel(request):
    """
    Handle the cancelled subscription (Stripe cancels the checkout session).
    """
    messages.warning(request, "Your subscription was cancelled.")
    return redirect(reverse('plans'))  # Redirect back to plans or another page


@login_required
def plans_view(request):
    """
    View to display available subscription plans from Stripe.
    """
    try:
        # Fetch all prices from Stripe
        stripe_prices = stripe.Price.list()
        price_map = {price.product: price.id for price in stripe_prices.data}

        plans = [
            {"name": "Basic Plan", "price_id": price_map.get(settings.STRIPE_PRICE_IDS["basic"]), "amount": 9.99},
            {"name": "Pro Plan", "price_id": price_map.get(settings.STRIPE_PRICE_IDS["pro"]), "amount": 19.99},
            {"name": "Premium Plan", "price_id": price_map.get(settings.STRIPE_PRICE_IDS["premium"]), "amount": 29.99},
        ]

        return render(request, "subscriptions/plans.html", {"plans": plans})

    except stripe.error.StripeError as e:
        return JsonResponse({"error": str(e)}, status=500)

