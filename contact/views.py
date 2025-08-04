from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm, NewsletterSignupForm
from .models import ContactMessage, NewsletterSubscriber


def send_confirmation_email(email):
    subject = "🌿 Welcome to Eco-Fitness!"
    message = (
        "Hi there,\n\n"
        "Thank you for subscribing to the Eco-Fitness newsletter!\n\n"
        "We're excited to have you on board. You'll be the first to receive:\n"
        "• Sustainable health and wellness tips\n"
        "• Eco-friendly workout ideas\n"
        "• Exclusive offers and updates from our green community\n\n"
        "Together, we can build a healthier body and a healthier planet.\n\n"
        "Stay tuned — your first eco-fitness tip is coming soon!\n\n"
        "Warm regards,\n"
        "The Eco-Fitness Team\n"
        f"{settings.DEFAULT_FROM_EMAIL}"
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )

def contact_view(request):
    contact_form = ContactForm()
    newsletter_form = NewsletterSignupForm()

    if request.method == "POST":
        if "message" in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                name = contact_form.cleaned_data["name"]
                email = contact_form.cleaned_data["email"]
                message = contact_form.cleaned_data["message"]

                ContactMessage.objects.create(
                    name=name, email=email, message=message)

                send_mail(
                    f"Contact Form Submission from {name}",
                    f"From: {email}\n\nMessage:\n{message}",
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )

                messages.success(request, "Your message has been sent!")
                return redirect("contact")

        elif "email" in request.POST and "message" not in request.POST:
            newsletter_form = NewsletterSignupForm(request.POST)
            if newsletter_form.is_valid():
                email = newsletter_form.cleaned_data["email"]
                if not NewsletterSubscriber.objects.filter(email=email).exists():
                    NewsletterSubscriber.objects.create(email=email)
                    send_confirmation_email(email)
                    messages.success(
                        request, "Thank you for subscribing! Check your inbox."
                    )
                else:
                    messages.info(request, "You're already subscribed.")
                return redirect("contact")

    return render(
        request,
        "contact/contact.html",
        {"contact_form": contact_form, "newsletter_form": newsletter_form},
    )
