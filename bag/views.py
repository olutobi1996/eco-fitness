from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product

def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """
    print(f"Received product_id: {product_id}")
    product = get_object_or_404(Product, pk=product_id)
    print(f"Retrieved product: {product}")  
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
    bag = request.session.get('bag', {})
    cart_items = []

    # Iterate over the products in the bag to get product details
    for product_id, product_data in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        cart_items.append({
            'product': product,
            'quantity': product_data['quantity'],
            'total': product.price * product_data['quantity']
        })

    return render(request, "bag/cart.html", {'cart_items': cart_items})


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
    """ Adjust the quantity of a specific product in the bag """
    product = get_object_or_404(Product, pk=item_id)
    try:
        quantity = int(request.POST.get('quantity', 0))
    except ValueError:
        messages.error(request, "Invalid quantity entered.")
        return redirect(reverse('view_bag'))
    
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})
    
    if str(item_id) in bag:
        if size:
            if size in bag[str(item_id)]['sizes']:
                if quantity > 0:
                    bag[str(item_id)]['sizes'][size] = quantity
                    messages.success(request, f'Updated {product.name} ({size.upper()}) quantity to {quantity}')
                else:
                    del bag[str(item_id)]['sizes'][size]
                    if not bag[str(item_id)]['sizes']:
                        del bag[str(item_id)]
                    messages.success(request, f'Removed {product.name} ({size.upper()}) from your bag')
        else:
            if quantity > 0:
                bag[str(item_id)]['quantity'] = quantity
                messages.success(request, f'Updated {product.name} quantity to {quantity}')
            else:
                del bag[str(item_id)]
                messages.success(request, f'Removed {product.name} from your bag')
    else:
        messages.error(request, "Product not found in your bag.")
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
