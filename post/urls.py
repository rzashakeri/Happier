from django.urls import path

from .views import upload_post_view

urlpatterns = [path("upload/", upload_post_view, name="upload_post")]
