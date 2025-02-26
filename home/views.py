from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home/index.html")  


def plans(request):
    return render(request, 'plans.html')

def reviews(request):
    return render(request, 'reviews.html')

def shop(request):
    return render(request, 'shop.html')

def community(request):
    return render(request, 'community.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')

def cart(request):
    return render(request, 'cart.html')

def product_list(request):
    return render(request, 'products/product_list.html') 


def add_product(request):
    return render(request, 'products/add_product.html')