import hashlib
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView
)
from cart.cart import Cart
from cart.forms import CartAddProductForm
from users.models import Profile
from .models import (
    Product
)


# 404 Not Found
def error404(request, exeption):
    word = "Похоже кто-то снова не будет спать, а исправлять ошибки!"
    return render(request, 'errors/err404.html', {'word': word,
                                                  'title': 'Not Found'})


# 500 Internal
def error500(request):
    word = "Похоже кто-то снова не будет спать, а исправлять ошибки!"
    return render(request, 'errors/err500.html', {'word': word,
                                                  'title': 'Internal'})


# 403 Forbidden
def error403(request, exeption):
    word = "Похоже кто-то снова не будет спать, а исправлять ошибки!"
    return render(request, 'errors/err403.html', {'word': word,
                                                  'title': 'Forbidden'})


# 400 Bad Request
def error400(request, exeption):
    word = "Похоже кто-то снова не будет спать, а исправлять ошибки!"
    return render(request, 'errors/err400.html', {'word': word,
                                                  'title': 'Bad Request'})


class HomePage(ListView):
    model = Product
    template_name = 'product/main.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/product.html', {'product': product,
                                                    'cart_product_form': cart_product_form,
                                                    'title': 'Товар'})


class CatalogPage(ListView):
    model = Product
    template_name = 'product/katalog.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        ctx = super(CatalogPage, self).get_context_data(**kwargs)
        ctx['title'] = 'Каталог'
        return ctx
