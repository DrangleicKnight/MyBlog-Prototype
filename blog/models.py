from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Tags(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="post")
    image = models.ImageField(upload_to="post_images", null = True)
    excerpt = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tags, related_name="post")
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("single_post", args = [self.slug])


class Comments(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.email