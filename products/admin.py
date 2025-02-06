from django.contrib import admin
from .models import Category, Product

# Custom admin for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')  # Display these fields in the list view
    search_fields = ('name', 'friendly_name')  # Add search functionality for these fields
    list_filter = ('name',)  # Add a filter sidebar based on 'name'

# Custom admin for Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'product_type', 'price', 'rating', 'created_at', 'updated_at')  # Fields to display
    list_filter = ('category', 'product_type', 'price', 'rating')  # Add filter options for these fields
    search_fields = ('name', 'sku', 'description')  # Add search functionality
    ordering = ('-created_at',)  # Order by created_at in descending order
    prepopulated_fields = {'sku': ('name',)}  # Automatically generate SKU based on the name (optional)

    # Custom fieldset for better organization in the form view
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'product_type', 'sku', 'description', 'price', 'rating')
        }),
        ('Images', {
            'fields': ('image_url', 'image')
        }),
        ('Additional Information', {
            'fields': ('duration_weeks', 'difficulty_level')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    # You can make the duration_weeks and difficulty_level fields readonly if they are not necessary for manual input.
    readonly_fields = ('created_at', 'updated_at')  # Make these fields readonly in the admin form

# Register models with their custom admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)




