from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from checkout.models import Order

from .forms import ProfileForm
from .models import AccountProfile


@login_required
def profile(request):
    profile = get_object_or_404(AccountProfile, user=request.user)
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    context = {
        "profile": profile,
        "orders": orders,
    }

    return render(request, "accounts/profile.html", context)

    return render(
        request,
        "accounts/profile.html",
        {
            "profile": profile,
            "orders": orders,
        },
    )


@login_required
def edit_profile(request):
    profile, created = AccountProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        shipping_address = request.POST.get("shipping_address")

        if form.is_valid():
            form.save()

            # Update profile
            if shipping_address:
                profile.shipping_address = shipping_address
                profile.save()

            messages.success(request, "Your profile was updated successfully.")
            return redirect("profile")

    else:
        form = ProfileForm(instance=request.user)

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form, "profile": profile},
    )
