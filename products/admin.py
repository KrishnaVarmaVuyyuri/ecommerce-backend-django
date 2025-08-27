from django.contrib import admin
from .models import Product
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at", "preview")

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
        return "No Image"

admin.site.register(Product, ProductAdmin)
