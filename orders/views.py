from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import OrderForm
from .models import (
    Orders,
    OrderItem,
)
from cart.cart import Cart


def orders_form(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            request.session['order_id'] = order.id

            return redirect(reverse('payment:payment_process'))
    else:
        form = OrderForm()

    return render(request, 'orders/order.html', {'form': form,
                                                 'cart': cart,
                                                 'title': 'Оформление заказа'})
