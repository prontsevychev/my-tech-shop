from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import BlogIndexView, BlogPostView


urlpatterns = [
    path('', BlogIndexView.as_view(), name='index'),
    path('<slug:post_slug>/', BlogPostView.as_view(), name='post'),
]
