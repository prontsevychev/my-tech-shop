from django.shortcuts import render, get_object_or_404
from .models import Post


def blog(request):
    return render(request, 'blog/blog.html', {})


def get_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    quotes = post.quotes.all()
    text_list = post.text.split("@@@") # "@@@" в тексте используется для указания места под цитату.
    text_last = text_list[-1]
    text_with_quotes = zip(text_list, quotes)
    return render(request, 'blog/blog_post.html', {
        'post':post,
        'text_with_quotes': text_with_quotes,
        'text_last': text_last,
    })
