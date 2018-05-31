from django.test import TestCase
from django.core import mail
from django.conf import settings
from django.shortcuts import reverse
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from constance import config

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
                rendered_page = render_to_string('blog/index.html', {
                    'index_post': self.index_post,
                    'request': request,
                    'config': config,
                })
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.content.decode("utf-8"), rendered_page)
                self.assertTemplateUsed(response, "blog/index.html")

    def test_post_view(self):
        for language_code, language in settings.LANGUAGES:
            with self.settings(LANGUAGE_CODE=language_code):
                path = "/{}test-slug/".format(_('blog/'))
                request = {'path': path}
                response = self.client.get(path)
                rendered_page = render_to_string('blog/post.html', {
                    'post': self.post,
                    'request': request,
                    'config': config,
                })
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.content.decode("utf-8"), rendered_page)
                self.assertTemplateUsed(response, "blog/post.html")


class ContactViewTest(TestCase):

    def test_send_message_form_submit(self):
        data = {'name': 'test_name',
                'email': 'test_email@email.com',
                'message': 'testing_message'}
        path = reverse("contact:index")
        response = self.client.post(path=path, data=data)
        body = render_to_string('contact/message.html', {'body': data})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, path)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Message from Contact-page")
        self.assertEqual(mail.outbox[0].body, body)
