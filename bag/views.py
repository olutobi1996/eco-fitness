from django.shortcuts import render

from django.shortcuts import render

def view_bag(request):
    return render(request, 'bag/bag.html')  # ✅ Ensure 'bag.html' exists

