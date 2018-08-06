import re
from urllib.parse import urljoin
from django.db import models
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"))
    slug = models.SlugField(_("Url-label"), max_length=100, unique=True)

    @property
    def content_with_quotes(self):
        quote_img_url = urljoin(settings.STATIC_URL, "blog/images/quote.png")
        quote_re = re.compile(r'\"(?P<quote>.+)\" \((?P<author>.+)\)\.')
        new_content = self.content
        for match in quote_re.finditer(self.content):
            if match:
                quote_dict = match.groupdict()
                quote_text = render_to_string(
                    'blog/quote.html',
                    {
                        'quote_img_url': quote_img_url,
                        'quote_dict': quote_dict
                    }
                )
                new_content = new_content.replace(match.group(0), quote_text)
        return new_content

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
