from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views


urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='index'),
    path('<slug:post_slug>/', views.BlogPostView.as_view(), name='post'),
]
