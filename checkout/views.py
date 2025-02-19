from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from .models import Order, OrderLineItem
from .forms import OrderForm
from products.models import Product
from bag.contexts import bag_contents
import stripe
from django.http import JsonResponse




def checkout(request):
    """ Handle checkout process """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST.get("street_address2", ""),
            "county": request.POST.get("county", ""),
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()

            # Process order items from session bag
            for item_id, item_data in bag.items():
                product = get_object_or_404(Product, pk=item_id)
                if isinstance(item_data, dict):  # If product has sizes
                    for size, quantity in item_data["sizes"].items():
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            product_size=size,
                            quantity=quantity,
                            lineitem_total=product.price * quantity,
                        )
                else:
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item_data,
                        lineitem_total=product.price * item_data,
                    )

            # Update order totals
            order.update_total()

            # Clear session bag after checkout
            del request.session["bag"]

            messages.success(request, f"Order placed successfully! Your order number is {order.order_number}.")
            return redirect(reverse("checkout_success", args=[order.order_number]))

        else:
            messages.error(request, "There was an error with your form. Please check your details.")

    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.info(request, "Your bag is empty.")
            return redirect(reverse("products"))

        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret if request.method != "POST" else None,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Display checkout success page """

    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f"Thank you for your order! Your order number is {order_number}.")
    
    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)

