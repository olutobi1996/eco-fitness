import json

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Subscription


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

    def handle_checkout_session_completed(self, event):
        """Handle the checkout.session.completed webhook from Stripe"""
        session = event.data.object
        user_email = session.get("customer_email")
        subscription_id = session.get("subscription")

        subscription = Subscription.objects.create(
            user_email=user_email,
            stripe_subscription_id=subscription_id,
            status="active",
        )

        self._send_subscription_email(user_email, subscription)

        return HttpResponse(
            content=json.dumps(
                {"message": "Checkout session completed and subscription created."}
            ),
            content_type="application/json",
            status=200,
        )

    def handle_invoice_payment_succeeded(self, event):
        """Handle the invoice.payment_succeeded webhook from Stripe"""
        invoice = event.data.object
        subscription_id = invoice.get("subscription")
        amount_paid = invoice.amount_paid / 100

        subscription = Subscription.objects.get(
            stripe_subscription_id=subscription_id)
        subscription.status = "active"
        subscription.amount_paid = amount_paid
        subscription.save()

        return HttpResponse(
            content=json.dumps(
                {"message": "Invoice payment succeeded and subscription updated."}
            ),
            content_type="application/json",
            status=200,
        )

    def handle_invoice_payment_failed(self, event):
        """Handle the invoice.payment_failed webhook from Stripe"""
        invoice = event.data.object
        subscription_id = invoice.get("subscription")

        subscription = Subscription.objects.get(
            stripe_subscription_id=subscription_id)
        subscription.status = "failed"
        subscription.save()

        return HttpResponse(
            content=json.dumps(
                {"message": "Invoice payment failed and subscription updated."}
            ),
            content_type="application/json",
            status=200,
        )

    def handle_customer_subscription_created(self, event):
        """Handle the customer.subscription.created webhook from Stripe"""
        subscription = event.data.object
        subscription_id = subscription.id
        user_email = subscription.customer_email
        status = subscription.status

        Subscription.objects.create(
            stripe_subscription_id=subscription_id,
            user_email=user_email,
            status=status,
        )

        return HttpResponse(
            content=json.dumps({"message": "Customer subscription created."}),
            content_type="application/json",
            status=200,
        )

    def handle_customer_subscription_deleted(self, event):
        """Handle the customer.subscription.deleted webhook from Stripe"""
        subscription = event.data.object
        subscription_id = subscription.id

        Subscription.objects.filter(stripe_subscription_id=subscription_id).update(
            status="canceled"
        )

        return HttpResponse(
            content=json.dumps(
                {"message": "Customer subscription deleted (canceled)."}
            ),
            content_type="application/json",
            status=200,
        )

    def _send_subscription_email(self, user_email, subscription):
        """Send the user a subscription confirmation email"""
        subject = render_to_string(
            "subscriptions/confirmation_emails/confirmation_email_subject.txt",
            {"subscription": subscription},
        )
        body = render_to_string(
            "subscriptions/confirmation_emails/confirmation_email_body.txt",
            {
                "subscription": subscription,
                "contact_email": settings.DEFAULT_FROM_EMAIL,
            },
        )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [user_email])
