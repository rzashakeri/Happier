from django.urls import path

from .views import profile_view

urlpatterns = [
    path('<str:username>/', profile_view, name='profile')
]
