from django.urls import path
from . import views
from .views import (
    payment_success,
    payment_error,
    balance,
    payment_alerts
)

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    # Payment
    path('alerts/', payment_alerts, name='alerts'),
    path('cart/balance/', balance, name='balance'),
    path('success/', payment_success, name='payment_success'),
    path('error/', payment_error, name='payment_error'),

]
