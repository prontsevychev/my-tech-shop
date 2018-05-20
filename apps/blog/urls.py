
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:post_slug>/', views.get_post, name='get_post'),
]
