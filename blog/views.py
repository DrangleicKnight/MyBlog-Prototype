from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Post, Author, Tags, Comments

from .forms import PostForm, CommentsForm


class Index(ListView):
    template_name = "blog.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        context = super().get_queryset()
        data = context[:3]
        return data


class CreatePost(CreateView):
    template_name = "add_post.html"
    model = Post
    form_class = PostForm
    success_url = "/"


class AllPosts(ListView):
    template_name = "all-posts.html"
    model = Post
    context_object_name = "all_posts"


class SinglePost(View):
    form = CommentsForm

    def get(self, request, slug):
        objected = Post.objects.get(slug=slug)

        context = {"posted" : objected,
                   "post_tags" : objected.tags.all(),
                   "comment_form" : self.form,
                   "comments" : objected.comments.all().order_by("id")}

        return render(request, "single_post.html", context)

    def post(self, request, slug):
        form = CommentsForm(request.POST)
        post = Post.objects.get(slug = slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect("/posts")

        request.session["read_later"] = slug

        context = {
            "comment_form" : form
        }
        return render(request, "single_post.html", context)


# class SinglePost(DetailView):
#     template_name = "single_post.html"
#     model = Post
#     context_object_name = "posted"


class ReadLater(TemplateView):
    template_name = "read_later.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        post_slug = self.request.session["read_later"]
        post = Post.objects.get(slug=post_slug)
        context["post"] = post
        return context

