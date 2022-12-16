from django.urls import path
from .views import (
    HomePage,
    CatalogPage,
    product_detail,
)

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('material/<slug>', product_detail, name="material"),
    path('catalog/', CatalogPage.as_view(), name="catalog"),
]
