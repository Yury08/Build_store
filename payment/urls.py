from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment/', views.payment_process, name='payment_process'),
    path('payment/success', views.success, name='success'),
    path('payment/error', views.error, name='error')

]
