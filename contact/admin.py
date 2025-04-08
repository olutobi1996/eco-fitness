from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'message')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
