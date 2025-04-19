from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm, NewsletterSignupForm
from .models import ContactMessage
from .models import NewsletterSubscriber


# View for Newsletter Sign-up
def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            # Add email to the newsletter list or Mailchimp
            email = form.cleaned_data['email']
            # Example of adding to Mailchimp (you need to configure the Mailchimp API)
            # mailchimp_api.add_to_newsletter_list(email)

            messages.success(request, "Thank you for subscribing to our newsletter!")
            return redirect('contact')  # Redirect back to the contact page or wherever you want
    else:
        form = NewsletterSignupForm()

    return render(request, 'contact/contact.html', {'form': form})


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