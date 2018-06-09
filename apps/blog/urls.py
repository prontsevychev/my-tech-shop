
from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:post_slug>/', views.post, name='post'),
]
