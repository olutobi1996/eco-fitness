import json
import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import (
    HttpResponse,
    get_object_or_404,
    redirect,
    render,
    reverse,
)
from django.views.decorators.http import require_POST

from bag.contexts import bag_contents
from products.models import Product

from .forms import OrderForm
from .models import Order, OrderLineItem


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": request.POST.get("save_info"),
                "username": str(request.user),
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now. Please try again later.",
        )
        return HttpResponse(content=str(e), status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})

        form_data = {
            "full_name": request.POST.get("full_name", ""),
            "email": request.POST.get("email", ""),
            "phone_number": request.POST.get("phone_number", ""),
            "country": request.POST.get("country", ""),
            "postcode": request.POST.get("postcode", ""),
            "town_or_city": request.POST.get("town_or_city", ""),
            "street_address1": request.POST.get("street_address1", ""),
            "street_address2": request.POST.get("street_address2", ""),
            "county": request.POST.get("county", ""),
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            # Create line items
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=int(item_id))
                    if isinstance(item_data, int):
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                    elif isinstance(item_data, dict) and "items_by_size" in item_data:
                        for size, quantity in item_data["items_by_size"].items():
                            OrderLineItem.objects.create(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products in your bag wasn't found in our database. "
                            "Please contact us for assistance."
                        ),
                    )
                    order.delete()
                    return redirect(reverse("view_bag"))

            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            messages.error(
                request,
                "There was an error with your form. Please double check your information.",
            )

    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment.")
            return redirect(reverse("products"))

        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)  # Amount in cents
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            # Prefill order form with user's info
            order_form = OrderForm(
                initial={
                    "full_name": request.user.get_full_name(),
                    "email": request.user.email,
                    "phone_number": getattr(request.user, "phone_number", ""),
                    "country": getattr(request.user, "country", ""),
                    "postcode": getattr(request.user, "postcode", ""),
                    "town_or_city": getattr(request.user, "town_or_city", ""),
                    "street_address1": getattr(request.user, "street_address1", ""),
                    "street_address2": getattr(request.user, "street_address2", ""),
                    "county": getattr(request.user, "county", ""),
                }
            )
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(
                request,
                "Stripe public key is missing. Did you forget to set it in your environment?",
            )

        context = {
            "order_form": order_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }
        return render(request, "checkout/checkout.html", context)


def checkout_success(request, order_number):
    """Handle successful checkouts"""
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        user = request.user
        order.user = user
        order.save()

        if save_info:
            # Assuming these fields exist on the user model or user profile
            user.phone_number = order.phone_number
            user.country = order.country
            user.postcode = order.postcode
            user.town_or_city = order.town_or_city
            user.street_address1 = order.street_address1
            user.street_address2 = order.street_address2
            user.county = order.county
            user.save()

    messages.success(
        request,
        f"Order successfully processed! Your order number is {order_number}. "
        f"A confirmation email will be sent to {order.email}.",
    )

    if "bag" in request.session:
        del request.session["bag"]

    return render(request, "checkout/checkout_success.html", {"order": order})
