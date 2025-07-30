from django.contrib import admin
from .models import AccountProfile

class AccountProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "shipping_address", "phone_number")  
    search_fields = ("user__username", "user__email")
    list_filter = ("user__is_active", "user__is_staff")
    ordering = ("user",)

admin.site.register(AccountProfile, AccountProfileAdmin)
