# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message in the database
            contact_message = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                # Send the email
                send_mail(
                    f"Message from {name}",
                    message,
                    email,  # Sender's email
                    [settings.CONTACT_EMAIL],  # Where the email should be sent
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
                return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


