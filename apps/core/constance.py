from django.utils.translation import gettext_lazy as _

ADDITIONAL_FIELDS = {
    'phone': ['phonenumber_field.formfields.PhoneNumberField', {}],
    'email': ['django.forms.EmailField', {}],
}

CONFIG = {
    'phone': ('+380 50 977 7126', _('Phone of company'), 'phone'),
    'address': ('Novosilna street, 1, Dnipro', _('Address of company'), str),
    'email': ('tech-shop@ukr.net', _('Email of company'), 'email'),
    'latitude': ('48.4498328', _('Latitude coordinate of company'), str),
    'longitude': ('35.0194117', _('Longitude coordinate of company'), str),
}
