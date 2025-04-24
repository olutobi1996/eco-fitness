from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):  # Keeping 'item_id' as per your preference
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1 if not provided
    redirect_url = request.POST.get('redirect_url')  # Get redirect_url from POST
    if not redirect_url:  # If not provided, default to 'view_bag'
        redirect_url = reverse('view_bag')
        print(f"Using default redirect URL: {redirect_url}")  # Debugging line

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    
    bag = request.session.get('bag', {})

    if size:
        # If item already in the bag, update size
        if str(item_id) in list(bag.keys()):
            if size in bag[str(item_id)]['items_by_size'].keys():
                bag[str(item_id)]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[str(item_id)]["items_by_size"][size]}')
            else:
                bag[str(item_id)]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[str(item_id)] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        # If no size, just add the item
        if str(item_id) in list(bag.keys()):
            bag[str(item_id)] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[str(item_id)]}')
        else:
            bag[str(item_id)] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    
    except Exception as e:

        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)