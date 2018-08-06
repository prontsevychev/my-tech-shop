# from django.shortcuts import render
#
#
# def index(request):
#     return render(request, 'shop/index.html', {})

from django.views.generic import TemplateView


class ShopIndexView(TemplateView):
    """Trying CBV"""
    template_name = 'shop/index.html'
