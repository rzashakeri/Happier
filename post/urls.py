from django.urls import path

from .views import like_view, post_view, show_post_view, create_new_post_view

urlpatterns = [
    path("post/like/<int:post_id>/", like_view, name="like"),
    path("post/<int:post_id>/", post_view, name="post"),
    path("post/<slug:slug>", show_post_view, name="show_post"),
    path("create/new/post/", create_new_post_view, name="upload_post"),
]
