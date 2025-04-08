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

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'comment')
    list_filter = ('rating', 'created_at')



# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)




