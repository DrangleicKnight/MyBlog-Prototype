from django.contrib import admin

from blog.models import Post, Author, Tags, Comments


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date", "tags")
    list_display = ("title", "author", "date")
    prepopulated_fields = {"slug" : ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tags)
admin.site.register(Comments)
