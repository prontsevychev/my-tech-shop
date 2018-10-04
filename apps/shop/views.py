from django.views.generic import TemplateView, DetailView

from .models import Product


class HomeView(TemplateView):
    template_name = "shop/index.html"


class ProductView(DetailView):
    model = Product
    template_name = "shop/product.html"
    slug_url_kwarg = "product_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alternative_products"] = Product.objects.filter(name=self.get_object().name)
        return context
