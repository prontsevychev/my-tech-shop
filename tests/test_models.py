from django.test import TestCase
from apps.blog.models import Post


class PostModelTests(TestCase):

    def setUp(self):
        Post.objects.create(title='Test title',
                            text='TestTestTest<quote>"Testing quote."(Testing author)</quote>TestTestTest.',
                            slug='test-slug')

    def test_text_with_quotes(self):
        post = Post.objects.get(slug='test-slug')
        self.assertEqual(post.text_with_quotes, """TestTestTest</p>
                        <div class="single_post_quote text-center">
                            <div class="quote_image"><img src="/static/blog/images/quote.png" alt=""></div>
                            <div class="quote_text">Testing quote.</div>
                            <div class="quote_name">Testing author</div>
                        </div>
                        <p>TestTestTest."""
                         )
