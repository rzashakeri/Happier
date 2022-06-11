from django.contrib import admin

from .models import VoicePost, ImagePost, VideoPost, TextPost, PostCategory

admin.site.register(ImagePost)
admin.site.register(VoicePost)
admin.site.register(VideoPost)
admin.site.register(TextPost)
admin.site.register(PostCategory)
