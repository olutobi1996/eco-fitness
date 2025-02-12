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

    for product_id, quantity in bag.items():
        try:
            product = Product.objects.get(id=product_id)
            subtotal = product.price * quantity
            total += subtotal
            product_count += quantity

            bag_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            continue  # Skip any invalid product IDs

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
        'eco_friendly_message': "You're just ${:.2f} away from free carbon-neutral shipping!".format(free_delivery_delta) if free_delivery_delta > 0 else "Enjoy free carbon-neutral shipping!",
    }

    return context
