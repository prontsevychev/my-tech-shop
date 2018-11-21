from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path(_('item/<slug:product_slug>/'), views.ProductView.as_view(), name='product'),
    path(_('cart/<int:cart_id>/'), views.CartView.as_view(), name='cart'),
    path(_('cart/<int:cart_id>/pay/'), views.CartPayView.as_view(), name='cart_pay'),
    path(_('cart/<int:cart_id>/pay-callback/'), views.CartPayCallbackView.as_view(), name='pay_callback'),
    path(_('cart/<int:cart_id>/pay-result/'), views.CartPayResultView.as_view(), name='pay_result'),
]
