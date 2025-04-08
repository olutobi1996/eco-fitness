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






