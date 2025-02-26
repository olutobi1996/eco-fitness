from django.contrib import admin
from .models import Category, Product

# Custom admin for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ('name', 'friendly_name')
    list_filter = ('name',)


# Custom admin for Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'rating', 'created_at', 'updated_at')
    list_filter = ('category', 'price', 'rating')
    search_fields = ('name', 'sku', 'description')
    ordering = ('-created_at',)
    prepopulated_fields = {'sku': ('name',)}

# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)





