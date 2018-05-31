from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Message


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('name', 'email', 'phone', 'message', )
        labels = {
            'name': "",
            'email': "",
            'phone': "",
            'message': "",
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _("Your name"),
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': _("Your email"),
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': _("Your phone number"),
            }),
            'message': forms.Textarea(attrs={
                'placeholder': _("Message"),
                'rows': 4,
            }),
        }
