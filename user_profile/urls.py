from django.urls import path

from .views import profile_view, edit_profile_view

urlpatterns = [
    path('<str:username>/', profile_view, name='profile'),
    path('accounts/edit', edit_profile_view, name='edit_profile')
]
