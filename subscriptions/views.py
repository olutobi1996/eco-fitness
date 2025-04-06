from django.shortcuts import render
import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
import os

# Load Stripe API key
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@csrf_exempt
def create_checkout_session(request, price_id):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='subscription',
            success_url="https://eco-fitness-2b6c5d715c47.herokuapp.com/success/", 
            cancel_url="https://eco-fitness-2b6c5d715c47.herokuapp.com/cancel/",   
        )
        
        return redirect(checkout_session.url)  # ✅ Redirect to Stripe Checkout page

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



def plans_view(request):
    try:
        # Fetch all prices from Stripe
        stripe_prices = stripe.Price.list()

        # Create a mapping of product IDs to prices
        price_map = {price.product: price.id for price in stripe_prices.data}
        print(price_map)
        # Define plans using settings
        plans = [
            {"name": "Basic Plan", "price_id": price_map.get(settings.STRIPE_PRICE_IDS["basic"]), "amount": 9.99},
            {"name": "Pro Plan", "price_id": price_map.get(settings.STRIPE_PRICE_IDS["pro"]), "amount": 19.99},
            {"name": "Premium Plan", "price_id": price_map.get(settings.STRIPE_PRICE_IDS["premium"]), "amount": 29.99},
        ]

        return render(request, "subscriptions/plans.html", {"plans": plans})

    except stripe.error.StripeError as e:
        return JsonResponse({"error": str(e)}, status=500)
