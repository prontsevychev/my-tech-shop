from datetime import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, View
from django.views.generic.edit import FormMixin

from liqpay.liqpay3 import LiqPay

from .forms import CartLineForm
from .models import Product, Cart


class HomeView(TemplateView):
    template_name = "shop/index.html"


class ProductView(FormMixin, DetailView):
    model = Product
    template_name = "shop/product.html"
    slug_url_kwarg = "product_slug"
    form_class = CartLineForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alternative_products"] = Product.objects.filter(name=self.get_object().name)
        return context

    def get_success_url(self):
        return reverse('shop:cart', kwargs={"cart_id": "1"})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.cart = Cart.objects.last()
        instance.product = self.get_object()
        instance.save()
        return super().form_valid(form)


class CartView(TemplateView):
    template_name = "shop/cart.html"


class CartPayView(TemplateView):
    template_name = 'shop/pay.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        cart = Cart.objects.get(pk=self.kwargs.get("cart_id"))
        params = {
            'action': 'pay',
            'amount': cart.get_total_cart_cost(),
            'currency': 'UAH',
            'description': f'Payment for {cart}',
            'order_id': str(datetime.now()),  # cart.pk
            'version': 3,
            'sandbox': settings.LIQPAY_SANDBOX_MODE,  # sandbox mode, set to 1 to enable it
            'server_url': 'http://' + request.get_host() + reverse('shop:pay_callback', kwargs={"cart_id": cart.pk}),
            'result_url': 'http://' + request.get_host() + reverse('shop:pay_result', kwargs={"cart_id": cart.pk}),
        }
        context = self.get_context_data(**kwargs)
        context.update({'signature': liqpay.cnb_signature(params), 'data': liqpay.cnb_data(params)})
        return self.render_to_response(context)


@method_decorator(csrf_exempt, name='dispatch')
class CartPayCallbackView(View):

    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)
        return HttpResponse()


@method_decorator(csrf_exempt, name='dispatch')
class CartPayResultView(DetailView):
    model = Cart
    template_name = 'shop/pay_result.html'
    pk_url_kwarg = 'cart_id'

    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        response = liqpay.decode_data_from_str(request.POST.get('data'))
        return super().get(request, *args, **kwargs)
