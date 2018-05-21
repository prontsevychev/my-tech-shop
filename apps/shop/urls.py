from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views


urlpatterns = [
    # path('', views.index, name='index'),  # url for function-based view
    path('', views.ShopIndexView.as_view(), name='index') # url for class-based view
]
