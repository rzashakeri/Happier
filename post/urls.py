from django.urls import path

from .views import like_view, post_view

urlpatterns = [
    path("like/<int:post_id>/", like_view, name="like"),
    path("<slug:slug>/", post_view, name="show_post"),
]
