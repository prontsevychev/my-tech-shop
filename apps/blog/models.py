from django.db import models


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    slug = models.SlugField("Url-метка", max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Quote(models.Model):
    post = models.ForeignKey('Post', models.CASCADE, related_name="quotes", verbose_name="Статья")
    author = models.CharField("Автор", max_length=200)
    text = models.TextField("Текст")

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"


