from django.urls import path
from . import views


urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("posts", views.blog_posts, name="blog_posts"),
    path("posts/<slug:slug>", views.blog_post_detail, name="blog_post_detail"),
]