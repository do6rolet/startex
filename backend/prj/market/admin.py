from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['articule', 'name', 'slug', 'price_in', 'price_out', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price_in', 'price_out', 'available']
