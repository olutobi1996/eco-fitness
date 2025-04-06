from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import AccountProfile  


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile(request):
    # Ensure the profile exists
    profile, created = AccountProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)

        # Handle the shipping address form
        shipping_address = request.POST.get('shipping_address')

        if form.is_valid():
            form.save()  # Save the User form

            # Save the shipping address if it's provided
            if shipping_address:
                profile.shipping_address = shipping_address
                profile.save()

            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {
        'form': form,
        'profile': profile
    })





