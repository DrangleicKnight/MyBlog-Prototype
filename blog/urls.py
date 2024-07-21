from django.urls import path

from .views import Index, AllPosts, SinglePost, CreatePost, ReadLater

urlpatterns = [
    path("", Index.as_view(), name = "starting-page"),
    path("posts/", AllPosts.as_view(), name = "posts"),
    path("posts/<slug:slug>", SinglePost.as_view(), name = "single_post"),
    path("add-post", CreatePost.as_view()),
    path("read-later", ReadLater.as_view())
]