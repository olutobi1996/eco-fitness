from django.shortcuts import render, get_object_or_404
from products.models import Product  

def index(request):
    product = get_object_or_404(Product, id=1)  
    return render(request, 'home/index.html', {'product': product})

def plans(request):
    return render(request, 'plans.html')

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