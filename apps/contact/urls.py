from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='index'),
]
