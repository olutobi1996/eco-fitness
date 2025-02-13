from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product

def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=product_id)
    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity < 1:
            messages.error(request, "Quantity must be at least 1.")
            return redirect(reverse('product_detail', args=[product_id]))
    except ValueError:
        messages.error(request, "Invalid quantity entered.")
        return redirect(reverse('product_detail', args=[product_id]))
    
    size = request.POST.get('product_size', None)
    redirect_url = request.POST.get('redirect_url', reverse('view_bag'))
    
    bag = request.session.get('bag', {})
    
    if str(product_id) in bag:
        if size:
            if size in bag[str(product_id)]['sizes']:
                bag[str(product_id)]['sizes'][size] += quantity
            else:
                bag[str(product_id)]['sizes'][size] = quantity
        else:
            bag[str(product_id)]['quantity'] += quantity
    else:
        bag[str(product_id)] = {'quantity': quantity, 'sizes': {size: quantity} if size else {}}
    
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
        if str(product_id) in bag:
            del bag[str(product_id)]
            messages.success(request, 'Item removed from your bag')
        else:
            messages.error(request, 'Item not found in your bag')
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect(reverse('view_bag'))

def adjust_bag(request, item_id):
    # Your logic here
    return redirect('some-view-name')
