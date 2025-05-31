from django.shortcuts import render, get_object_or_404
from products.models import Product  
from home.models import HeroImage 

def index(request):
    product = Product.objects.first()
    hero = HeroImage.objects.filter(active=True).first()  
    
    context = {
        'product': product,
        'hero': hero,
    }
    return render(request, 'home/index.html', context)


def profile(request):
    return render(request, 'accounts/profile.html')


def cart(request):
    return render(request, 'cart.html')

def product_list(request):
    return render(request, 'products/product_list.html') 


def add_product(request):
    return render(request, 'products/add_product.html')


def handler404(request, exception):
    """ Custom 404 Error Handler - Page Not Found """
    return render(request, "errors/404.html", status=404)
