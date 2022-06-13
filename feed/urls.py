from django.urls import path

from .views import feed

urlpatterns = [path("", feed, name="feed")]
