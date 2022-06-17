from django.contrib import admin

from .models import Post, PostAttachment, Audio

admin.site.register(Post)
admin.site.register(PostAttachment)
admin.site.register(Audio)
