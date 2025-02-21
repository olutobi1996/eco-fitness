from django.http import HttpResponse
import json

class StripeWH_Handler:
    """Handle Stripe webhooks"""

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
        print(f"🔔 Payment succeeded for {intent.amount / 100} {intent.currency.upper()}")

        return HttpResponse(
            content=json.dumps({'message': f'Successful payment: {event["type"]}'}),
            content_type="application/json",
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        intent = event.data.object
        print(f"⚠️ Payment failed for {intent.amount / 100} {intent.currency.upper()}")

        return HttpResponse(
            content=json.dumps({'message': f'Failed payment: {event["type"]}'}),
            content_type="application/json",
            status=200
        )
