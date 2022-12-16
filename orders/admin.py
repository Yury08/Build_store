from django.contrib import admin
from .models import (
    OrderItem,
    Orders
)


class OrederItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'city', 'created', 'updated', 'paid']
    list_filter = ['created', 'updated', 'paid']
    inlines = [OrederItemAdmin]  # Сдесь должен быть класс, а не модель
