from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import HomeView, ProductView, CartView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path(_('item/<slug:product_slug>/'), ProductView.as_view(), name='product'),
    path(_('cart/<int:cart_id>/'), CartView.as_view(), name='cart'),
]
