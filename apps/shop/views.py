from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import reverse

from .models import Product, Cart
from .forms import CartLineForm


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


class CartView(DetailView):
    model = Cart
    template_name = "shop/cart.html"
    pk_url_kwarg = "cart_id"
