from django.db import models
import re


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    slug = models.SlugField("Url-метка", max_length=100, unique=True)

    @property
    def text_with_quotes(self):
        quote_re = re.compile(r'<quote>\"(?P<quote>.+)\"\((?P<author>.+)\)</quote>')
        match = quote_re.search(self.text)
        if match:
            quote_dict = match.groupdict()
            quote_text = f"""</p>
                        <div class="single_post_quote text-center">
                            <div class="quote_image"><img src="/static/blog/images/quote.png" alt=""></div>
                            <div class="quote_text">{quote_dict['quote']}</div>
                            <div class="quote_name">{quote_dict['author']}</div>
                        </div>
                        <p>"""
            text_with_quotes = quote_re.sub(quote_text, self.text)
        else:
            text_with_quotes = self.text
        return text_with_quotes

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
