from django import forms

from .models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"
        exclude = ["post"]


