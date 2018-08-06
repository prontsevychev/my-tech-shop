from modeltranslation.translator import translator, TranslationOptions
from .models import Post


class PostTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Post.
    """

    fields = ('title', 'content', )


translator.register(Post, PostTranslationOptions)
