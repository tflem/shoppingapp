from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity')

admin.site.register(Product, ProductAdmin)
