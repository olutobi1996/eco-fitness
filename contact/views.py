from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm, NewsletterSignupForm
from .models import ContactMessage, NewsletterSubscriber

# Sending confirmation email
def send_confirmation_email(email):
    subject = '🌿 Welcome to Eco-Fitness!'
    message = 'Thanks for subscribing to our eco-friendly fitness newsletter. You’ll get the latest green fitness tips, gear, and offers!'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

# View for Newsletter Sign-up
def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
                send_confirmation_email(email)  
                messages.success(request, "Thank you for subscribing! Check your inbox.")
            else:
                messages.info(request, "You’re already subscribed!")

            return redirect('contact') 
    else:
        form = NewsletterSignupForm()

    return render(request, 'contact/contact.html', {'form': form})
