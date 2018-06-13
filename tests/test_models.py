from django.test import TestCase
from django.conf import settings
from django.template.loader import render_to_string
from apps.blog.models import Post


class PostModelMethodsTests(TestCase):

    def setUp(self):
        self.post_with_quote = Post.objects.create(
            title='Test title',
            content='TestTestTest"Testing quote." (Testing author).\n"Test2" (Test2).TestTestTest.',
            slug='test-slug'
        )
        self.post_without_quote = Post.objects.create(
            title='Test title',
            content='TestTestTest"Testing quote."(Testing author)TestTestTest.',
            slug='test2-slug'
        )

    def test_method_content_with_quotes(self):
        quote_img_url = settings.STATIC_URL + "blog/images/quote.png"
        test_dict1 = {'quote': "Testing quote.", 'author': "Testing author"}
        test_dict2 = {'quote': "Test2", 'author': "Test2"}
        rendered1 = render_to_string(
            'blog/quote.html',
            {
                'quote_img_url': quote_img_url,
                'quote_dict': test_dict1
            }
        )
        rendered2 = render_to_string(
            'blog/quote.html',
            {
                'quote_img_url': quote_img_url,
                'quote_dict': test_dict2
            }
        )
        self.assertEqual(
            self.post_with_quote.content_with_quotes,
            "TestTestTest" + rendered1 + "\n" +rendered2 + "TestTestTest."
        )
        self.assertEqual(
            self.post_without_quote.content_with_quotes,
            """TestTestTest"Testing quote."(Testing author)TestTestTest."""
        )
