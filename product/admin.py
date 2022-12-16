from django.contrib import admin
from .models import (
    Product
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'available']
    list_filter = ['available', ]
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
