from django import template
from django.urls import translate_url


register = template.Library()


@register.simple_tag()
def translate_url_tag(path, language_code):
    new_path = translate_url(path, language_code)
    return new_path
