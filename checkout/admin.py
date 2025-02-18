from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ Inline admin for order line items, ensuring clarity and ease of use """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0  # Prevents extra empty fields from appearing


class OrderAdmin(admin.ModelAdmin):
    """ Admin panel configuration for orders """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created_at',
                       'delivery_cost', 'order_total', 'grand_total')

    fields = ('order_number', 'created_at', 'full_name',
              'email', 'phone_number', 'country', 'postcode', 
              'city', 'address_line1', 'address_line2', 
              'state_or_region', 'delivery_cost', 
              'order_total', 'grand_total')

    list_display = ('order_number', 'created_at', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total')

    list_filter = ('created_at', 'grand_total', 'delivery_cost')
    search_fields = ('order_number', 'full_name', 'email')
    
    ordering = ('-created_at',)  # Newest orders appear first


admin.site.register(Order, OrderAdmin)
