from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})
    
    if product_id in bag:
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity
    
    request.session['bag'] = bag
    messages.success(request, f'Added {quantity} x {product.name} to your bag')
    
    return redirect(redirect_url)


def view_bag(request):
    """ A view to render the shopping bag page """
    return render(request, 'bag/bag.html')


def remove_from_bag(request, product_id):
    """ Remove an item from the shopping bag """
    try:
        bag = request.session.get('bag', {})
        
        if product_id in bag:
            del bag[product_id]
        
        request.session['bag'] = bag
        messages.success(request, 'Item removed from your bag')
        
        return redirect(reverse('view_bag'))
    
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect(reverse('view_bag'))

