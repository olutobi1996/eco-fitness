# about_us/views.py
from django.shortcuts import render

from .models import AboutUs


def about_us_view(request):
    try:
        about_us = AboutUs.objects.all().first()
    except AboutUs.DoesNotExist:
        about_us = None
    return render(request, "about_us/about_us.html", {"about_us": about_us})
