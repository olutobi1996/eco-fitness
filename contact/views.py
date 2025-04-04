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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f"New Contact Form Submission from {name}",
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,  # ✅ Fixed sender email
                    recipient_list=[settings.CONTACT_EMAIL],  # ✅ Uses contact email from settings
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f"Error sending email: {str(e)}")
                return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})




