import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Product
from users.models import Profile
from .cart import Cart
from .forms import (
    CartAddProductForm,
)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    title = 'Корзина'
    return render(request, 'cart/market.html', {
        'cart': cart,
        'title': title
    })


# Payment


def balance(request):
    merchant_id = '21947'
    secret_word = 'uVy@S.V+ht2m55)'
    currency = 'RUB'
    order_id = '150'
    order_amount = '101.04'
    sign = hashlib.md5(
        f'{merchant_id}:{order_amount}:{secret_word}:{currency}:{order_id}'.encode('utf-8')).hexdigest()

    context = {
        'm': merchant_id,
        'oa': order_amount,
        'o': order_id,
        's': sign,
        'currency': currency,
    }

    return render(request, 'cart/balance.html', context)


# Суда приходят данные с URL оповещения. Вот тут и проблема в том что в переменную amount ничего не присваивается.
def payment_alerts(request):
    amount = request.GET.get("AMOUNT")
    current_user = Profile.objects.get(pk=request.user.id)
    current_user.balance = current_user.balance + amount
    current_user.save()


# Страница о успешной оплате
def payment_success(request):
    return render(request, 'payment/success.html', {'title': 'Успешно!'})


# страница при ошибках оплаты
def payment_error(request):
    return render(request, 'payment/error.html', {'title': 'Ошибка!'})
