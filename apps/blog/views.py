from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Post


class BlogIndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    # extra_context = {"index_post": get_object_or_404(Post, slug="vivamus_sed_nunc")}  # тест крашится

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['index_post'] = get_object_or_404(Post, slug="vivamus_sed_nunc")  # тест не крашится
        return context


class BlogPostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
