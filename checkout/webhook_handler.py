from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product
import json
import stripe
import time 

from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product
import json
import stripe
import time

class StripeWH_Handler:
    """🌱 Handle Stripe webhooks for eco-friendly eCommerce"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=json.dumps({'message': f'Unhandled event: {event["type"]}'}),
            content_type="application/json",
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.get('bag', '{}')  # Ensure default value if missing
        save_info = intent.metadata.get('save_info', False)

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Log payment success
        print(f"✅ Payment succeeded for {grand_total} {intent.currency.upper()} (PID: {pid})")

        # Clean empty address fields
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

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
                content=json.dumps({'message': 'Order already exists, skipping creation.'}),
                content_type="application/json",
                status=200
            )

        # Order doesn't exist, create it
        try:
            order = Order.objects.create(
                full_name=shipping_details.name,
                email=billing_details.email,
                phone_number=shipping_details.phone,
                country=shipping_details.address.country,
                postcode=shipping_details.address.postal_code,
                town_or_city=shipping_details.address.city,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                county=shipping_details.address.state,
                original_bag=bag,
                stripe_pid=pid,
            )

            # Process order items
            for item_id, item_data in json.loads(bag).items():
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):  # Simple quantity case
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                else:  # Case with different sizes
                    for size, quantity in item_data['items_by_size'].items():
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size,
                        )

            return HttpResponse(
                content=json.dumps({'message': 'Order created successfully!'}),
                content_type="application/json",
                status=200
            )

        except Exception as e:
            if order:
                order.delete()  # Rollback order if creation fails
            return HttpResponse(
                content=json.dumps({'error': str(e)}),
                content_type="application/json",
                status=500
            )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        intent = event.data.object
        print(f"⚠️ Payment failed for {intent.amount / 100} {intent.currency.upper()} (PID: {intent.id})")

        return HttpResponse(
            content=json.dumps({'message': 'Payment failed.'}),
            content_type="application/json",
            status=200
        )

