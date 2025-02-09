from django.contrib import admin
from .models import Category, Product, DietPlan, FitnessPlan  # Ensure DietPlan is imported

# Custom admin for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')
    search_fields = ('name', 'friendly_name')
    list_filter = ('name',)

# Custom admin for Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'product_type', 'price', 'rating', 'created_at', 'updated_at')
    list_filter = ('category', 'product_type', 'price', 'rating')
    search_fields = ('name', 'sku', 'description')
    ordering = ('-created_at',)
    prepopulated_fields = {'sku': ('name',)}


class FitnessPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_weeks', 'created_at')  # ✅ Removed difficulty_level
    list_filter = ('price', 'duration_weeks')  # ✅ Removed difficulty_level 

fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'duration_weeks', 'difficulty_level', 'image')  # ✅ Correct fields
        }),
    )

# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(DietPlan)  # ✅ Ensure DietPlan is registered
admin.site.register(FitnessPlan, FitnessPlanAdmin)  # ✅ Register properly




