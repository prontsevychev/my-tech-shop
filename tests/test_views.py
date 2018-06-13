from django.test import TestCase
from django.urls import reverse
from apps.blog.models import Post


class BlogViewTests(TestCase):

    def setUp(self):
        Post.objects.create(
            title='Test title',
            content='TestTestTest"Testing quote." (Testing author).TestTestTest.',
            slug='test-slug'
        )

    def test_blog_view(self):
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, "Technological Blog")
        self.assertContains(response, "Vivamus sed nunc in arcu cursus mollis quis et orci. Interdum et malesuada.")
        self.assertTemplateUsed(response, "blog/index.html")
        self.assertEqual(response.status_code, 200)

    def test_post_view(self):
        post = Post.objects.get(slug='test-slug')
        response = self.client.get('/blog/test-slug/')
        self.assertContains(response, 'Test title')
        self.assertEqual(response.context['post'], post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post.html")
