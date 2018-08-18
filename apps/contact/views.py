from django.views.generic import FormView
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.template.loader import render_to_string

from .models import Message
from .forms import MessageForm


class ContactView(FormView):
    model = Message
    template_name = 'contact/index.html'
    form_class = MessageForm

    def get_success_url(self):
        return reverse('contact:index')

    def form_valid(self, form):
        form.save()
        message = render_to_string('contact/message.html', {'body': form.cleaned_data,})
        send_mail(
            _("Message from Contact-page"),
            message,
            None,
            ['tech-shop@ukr.net'],
        )
        return super(ContactView, self).form_valid(form)
