import braintree
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Orders


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Orders, id=order_id)

    if request.method == 'POST':
        # Получение токена для создания транзакции
        nonce = request.POST.get('payment_method_nonce', None)
        # Создание и хранение транзакции
        result = braintree.Transaction.sale({
            'amount': order.get_total_cost(),
            'payment_method_nonce': nonce,  # токен, сгенерированный Braintree для платежной транзакции
            'options': {
                'submit_for_settlement': True
                # дополнительные параметры. Мы передали значение submit_for_settlement, равное True, благодаря чему транзакция будет обрабатываться автоматически
            }
        })
        if result.is_success:
            # Отметка заказа, как оплаченного
            order.paid = True
            # Сохранение id транзакции в заказе
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:success')
        else:
            return redirect('payment:error')
    else:
        # Формирование одноразового токена для JavaScript SDK.
        client_token = braintree.ClientToken.generate()
        return render(request, 'payment/process.html',
                      {'order': order, 'client_token': client_token, 'title': 'Оплата'})


# Страница о успешной оплате
def success(request):
    return render(request, 'payment/success.html', {'title': 'Успешно!'})


# страница при ошибках оплаты
def error(request):
    return render(request, 'payment/error.html', {'title': 'Ошибка!'})
