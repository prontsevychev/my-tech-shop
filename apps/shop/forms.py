from django import forms
from django.utils.translation import gettext_lazy as _

from .models import CartLine


class CartLineForm(forms.ModelForm):

    class Meta:
        model = CartLine
        fields = ('quantity', )
