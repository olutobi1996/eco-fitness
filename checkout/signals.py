from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_order_on_save(sender, instance, **kwargs):
    """
    Update the order total whenever a line item is added or updated.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_order_on_delete(sender, instance, **kwargs):
    """
    Update the order total when a line item is deleted.
    """
    instance.order.update_total()
