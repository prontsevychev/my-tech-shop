from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Message(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    email = models.EmailField(_("Email"))
    phone = PhoneNumberField(_("Phone"), blank=True, null=True)
    message = models.TextField(_("Message"))

    def __str__(self):
        return "{0} -- [{1}]".format(self.name, self.email)

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
