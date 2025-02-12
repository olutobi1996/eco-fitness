from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    """ Context processor for shopping bag details """

    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        
        # Handling products without sizes
        if isinstance(item_data, dict):
            quantity = item_data.get('quantity', 0)
            sizes = item_data.get('sizes', {})

            # Add main quantity if present
            if quantity:
                subtotal = product.price * quantity
                total += subtotal
                product_count += quantity
                bag_items.append({
                    'product': product,
                    'quantity': quantity,
                    'subtotal': subtotal,
                })

            # Handle size-based quantities
            for size, size_quantity in sizes.items():
                subtotal = product.price * size_quantity
                total += subtotal
                product_count += size_quantity
                bag_items.append({
                    'product': product,
                    'quantity': size_quantity,
                    'subtotal': subtotal,
                    'size': size,
                })
        else:
            continue  # Ignore invalid entries

    # Calculate delivery cost
    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)
    standard_delivery_rate = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / 100

    if total < free_delivery_threshold:
        delivery = total * standard_delivery_rate
        free_delivery_delta = free_delivery_threshold - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
        'eco_friendly_message': f"You're just ${free_delivery_delta:.2f} away from free carbon-neutral shipping!" if free_delivery_delta > 0 else "Enjoy free carbon-neutral shipping!",
    }

    return context

