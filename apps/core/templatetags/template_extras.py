from django import template
from django.urls import translate_url
from django import forms

register = template.Library()


@register.simple_tag()
def translate_url_tag(path, language_code):
    new_path = translate_url(path, language_code)
    return new_path


@register.simple_tag()
def add_class_id_to_form_field_tag(field, field_class, field_id):
    return field.as_widget(
        attrs={
            'id': field_id,
            'class': field_class,
        }
    )
