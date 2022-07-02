from django.urls import path

from .views import create_comment

urlpatterns = [path("create/<int:post_id>/", create_comment, name="create_comment")]
