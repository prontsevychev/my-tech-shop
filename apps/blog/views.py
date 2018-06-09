from django.shortcuts import render, get_object_or_404
from .models import Post


def blog(request):
    return render(request, 'blog/blog.html', {})


def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, 'blog/blog_post.html', {'post': post})
