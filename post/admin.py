from django.contrib import admin

from .models import Post, Audio, Video, Image, Like

admin.site.register(Post)
admin.site.register(Audio)
admin.site.register(Video)
admin.site.register(Image)
admin.site.register(Like)
