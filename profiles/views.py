from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm

@login_required
def profile(request):
    """ Display and update the user's profile """
    user_profile = get_object_or_404(UserProfile, user=request.user)  

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')  # Prevents resubmission issues
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserProfileForm(instance=user_profile)

    orders = user_profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def edit_profile(request):
    """ Allow users to edit their profile details """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(request, 'profiles/edit_profile.html', context)


@login_required
def order_history(request, order_number):
    """ Display details of a past order """
    order = get_object_or_404(Order, order_number=order_number, user_profile__user=request.user)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, 'profiles/order_history.html', context)


