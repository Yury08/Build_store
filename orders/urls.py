from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.orders_form, name='order_form')
]
