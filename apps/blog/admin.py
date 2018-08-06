from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from . import models


class PostAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(models.Post, PostAdmin)
