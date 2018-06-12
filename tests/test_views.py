from django.test import TestCase
from django.urls import reverse
from apps.blog.models import Post


class BlogViewTests(TestCase):

    def setUp(self):
        Post.objects.create(title='Test title',
                            text='TestTestTest<quote>"Testing quote."(Testing author)</quote>TestTestTest.',
                            slug='test-slug')

    def test_blog_view(self):
        response = self.client.get(reverse('blog:blog'))
        self.assertContains(response, "Technological Blog")
        self.assertContains(response, "Vivamus sed nunc in arcu cursus mollis quis et orci. Interdum et malesuada.")

    def test_post_view(self):
        post = Post.objects.get(slug='test-slug')
        response = self.client.get('/blog/test-slug/')
        self.assertContains(response, 'Test title')
        self.assertEqual(response.context['post'], post)
