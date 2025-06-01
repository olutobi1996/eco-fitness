import json
import time

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

# Make sure this import path is correct
from accounts.models import AccountProfile
from products.models import Product

from .models import Order, OrderLineItem


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=json.dumps(
                {"message": f'Unhandled event: {event["type"]}'}),
            content_type="application/json",
            status=200,
        )

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.get("bag", "{}")
        save_info = intent.metadata.get("save_info", False)

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        print(
            f"✅ Payment succeeded for {grand_total} {intent.currency.upper()} (PID: {pid})"
        )

        # Clean empty shipping address fields
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Get profile if user exists
        profile = None
        username = intent.metadata.get("username", "AnonymousUser")
        if username != "AnonymousUser":
            try:
                profile = AccountProfile.objects.get(user__username=username)
            except AccountProfile.DoesNotExist:
                profile = None

        # Update profile if save_info is True
        if profile and save_info:
            profile.default_phone_number = shipping_details.phone
            profile.default_country = shipping_details.address.country
            profile.default_postcode = shipping_details.address.postal_code
            profile.default_town_or_city = shipping_details.address.city
            profile.default_street_address1 = shipping_details.address.line1
            profile.default_street_address2 = shipping_details.address.line2
            profile.default_county = shipping_details.address.state
            profile.save()

        # Check if order already exists, retry up to 5 times
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=json.dumps(
                    {"message": "Order already exists, skipping creation."}
                ),
                content_type="application/json",
                status=200,
            )

        # Create order if it doesn't exist
        try:
            order = Order.objects.create(
                full_name=shipping_details.name,
                user_profile=profile,
                email=billing_details.email,
                phone_number=shipping_details.phone,
                country=shipping_details.address.country,
                postcode=shipping_details.address.postal_code,
                town_or_city=shipping_details.address.city,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                county=shipping_details.address.state,
                grand_total=grand_total,
                original_bag=bag,
                stripe_pid=pid,
            )

            # Create line items
            for item_id, item_data in json.loads(bag).items():
                product = Product.objects.get(id=item_id)
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
        except Exception as e:
            if order:
                order.delete()
            return HttpResponse(
                content=json.dumps({"error": str(e)}),
                content_type="application/json",
                status=500,
            )

        # Send confirmation email
        self._send_confirmation_email(order)

        return HttpResponse(
            content=json.dumps({"message": "PaymentIntent succeeded"}),
            content_type="application/json",
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content=json.dumps({"message": "Payment failed"}),
            content_type="application/json",
            status=200,
        )
