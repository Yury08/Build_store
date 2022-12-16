from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('cart/cart/orders/', include('orders.urls', namespace='orders')),
    path('', include('product.urls')),
]

"""
    400 Bad Request
    403 Forbidden
    404 Not Found
    500 Internal
"""

handler400 = 'product.views.error400'
handler403 = 'product.views.error403'
handler404 = 'product.views.error404'
handler500 = 'product.views.error500'

if settings.DEBUG:
    urlpatterns = [
                      path('__debug__/', include('debug_toolbar.urls')),
                  ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
