from django.urls import path

from .views import like_view, post_view, show_post_view

urlpatterns = [
    path("like/<int:post_id>/", like_view, name="like"),
    path("<int:post_id>/", post_view, name="post"),
    path("<slug:slug>", show_post_view, name="show_post"),
]
