from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse('view_bag'))

    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})
    item_id_str = str(item_id)

    if size:
        if item_id_str in bag:
            if 'items_by_size' not in bag[item_id_str]:
                bag[item_id_str]['items_by_size'] = {}
            if size in bag[item_id_str]['items_by_size']:
                bag[item_id_str]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id_str]["items_by_size"][size]}')
            else:
                bag[item_id_str]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id_str] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id_str in bag:
            if isinstance(bag[item_id_str], dict):
                # Fallback: convert to integer if stored differently
                bag[item_id_str] = quantity
            else:
                bag[item_id_str] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id_str]}')
        else:
            bag[item_id_str] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})
    item_id_str = str(item_id)

    if size:
        if quantity > 0:
            if item_id_str in bag and 'items_by_size' in bag[item_id_str]:
                bag[item_id_str]['items_by_size'][size] = quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id_str]["items_by_size"][size]}')
        else:
            if item_id_str in bag and 'items_by_size' in bag[item_id_str]:
                bag[item_id_str]['items_by_size'].pop(size, None)
                if not bag[item_id_str]['items_by_size']:
                    bag.pop(item_id_str)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id_str] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id_str]}')
        else:
            bag.pop(item_id_str, None)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    try:
        size = request.POST.get('product_size')
        bag = request.session.get('bag', {})
        item_id_str = str(item_id)

        if size:
            if item_id_str in bag and 'items_by_size' in bag[item_id_str]:
                bag[item_id_str]['items_by_size'].pop(size, None)
                if not bag[item_id_str]['items_by_size']:
                    bag.pop(item_id_str)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id_str, None)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
