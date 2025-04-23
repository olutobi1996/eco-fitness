from decimal import Decimal
from django import template
from .custom_filters import *

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    try:
        price = Decimal(price)
        quantity = int(quantity)
        return price * quantity
    except (TypeError, ValueError):
        return "Error: Invalid input"
