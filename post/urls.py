from django.urls import path

from .views import like_view, post_view, create_comment_view

urlpatterns = [
    path("like/<int:post_id>/", like_view, name="like"),
    path("<slug:slug>/", post_view, name="show_post"),
    path("comment/create/<int:post_id>/", create_comment_view, name="create_comment"),
]
