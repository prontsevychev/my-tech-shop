from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

from apps.blog.models import Post


class BlogViewTests(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title_ru='Тестовый заголовок',
            title_en='Test title',
            content='TestTestTest"Testing quote." (Testing author).TestTestTest.',
            slug='test-slug'
        )
        self.index_post = Post.objects.create(
            title='Test2',
            content='TestTestTest"Testing quote." (Testing author).TestTestTest.',
            slug='vivamus_sed_nunc'
        )

    def test_blog_view(self):
        for language_code, language in settings.LANGUAGES:
            with self.settings(LANGUAGE_CODE=language_code):
                path = "/{}".format(_('blog/'))
                request = {'path': path}
                response = self.client.get(path)
                rendered_page = render_to_string('blog/index.html', {'index_post': self.index_post, 'request': request})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.content.decode("utf-8"), rendered_page)
                self.assertTemplateUsed(response, "blog/index.html")

    def test_post_view(self):
        for language_code, language in settings.LANGUAGES:
            with self.settings(LANGUAGE_CODE=language_code):
                path = "/{}test-slug/".format(_('blog/'))
                request = {'path': path}
                response = self.client.get(path)
                rendered_page = render_to_string('blog/post.html', {'post': self.post, 'request': request})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.content.decode("utf-8"), rendered_page)
                self.assertTemplateUsed(response, "blog/post.html")
