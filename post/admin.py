from django.contrib import admin

from .models import PostComment, PostCategory

admin.site.register(PostComment)
admin.site.register(PostCategory)
