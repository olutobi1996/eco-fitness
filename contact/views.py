from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage
from .forms import NewsletterForm
from .models import NewsletterSubscriber
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


# Initialize Mailchimp Client
mailchimp = Client()
mailchimp.set_config({
    "api_key": settings.MAILCHIMP_API_KEY,
    "server": settings.MAILCHIMP_SERVER_PREFIX  # e.g., "us1" or "us2"
})

# Define the list ID for your Mailchimp audience (list)
MAILCHIMP_LIST_ID = settings.MAILCHIMP_LIST_ID

# View for Newsletter Sign-up
def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Add to Mailchimp list
            try:
                # Add subscriber to Mailchimp
                response = mailchimp.lists.add_list_member(MAILCHIMP_LIST_ID, {
                    "email_address": email,
                    "status": "subscribed",  # "subscribed", "unsubscribed", "cleaned", or "pending"
                })
                
                # Save subscriber in your local DB (optional)
                NewsletterSubscriber.objects.create(email=email)
                
                # Send confirmation email (Optional)
                send_confirmation_email(email)

                messages.success(request, 'You have successfully signed up for our newsletter!')
                return redirect('newsletter_signup')
            except ApiClientError as e:
                print(f"Error: {e.text}")
                messages.error(request, 'There was an issue with your signup. Please try again.')
                return redirect('newsletter_signup')
        else:
            messages.error(request, 'Please enter a valid email address.')

    else:
        form = NewsletterForm()

    return render(request, 'newsletter/signup.html', {'form': form})


# Sending confirmation email
def send_confirmation_email(email):
    subject = 'Welcome to Our Newsletter!'
    message = 'Thank you for signing up for our newsletter. Stay tuned for exciting updates!'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

# Contact view for handling contact form submissions
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(name=name, email=email, message=message)

            sender_email = settings.DEFAULT_FROM_EMAIL  

            try:
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=f"From: {email}\n\n{message}",  
                    from_email=sender_email, 
                    recipient_list=[settings.CONTACT_EMAIL],  
                    fail_silently=False,  
                )

                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')

            except Exception as e:
                print(f"❌ Email Error: {e}")  
                messages.error(request, "There was an error sending your message.")
                return redirect('contact')

        else:
            messages.error(request, 'Please correct the errors in the form.')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})