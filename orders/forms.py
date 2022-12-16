from django import forms
from django.forms import TextInput

from .models import (
    OrderItem,
    Orders,
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'email', 'address', 'city')
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': TextInput(attrs={'placeholder': 'Фамилия'}),
            'email': TextInput(attrs={'placeholder': 'Почта'}),
            'address': TextInput(attrs={'placeholder': 'Адрес'}),
            'city': TextInput(attrs={'placeholder': 'город'}),
        }
