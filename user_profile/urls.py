from django.urls import path

from .views import (
    profile_view,
    edit_profile_view,
    delete_account_view,
    edit_personal_information,
)

urlpatterns = [
    path("<str:username>/", profile_view, name="profile"),
    path("accounts/edit/profile", edit_profile_view, name="edit_profile"),
    path(
        "accounts/edit/personal-information",
        edit_personal_information,
        name="edit_personal_information",
    ),
    path("accounts/delete", delete_account_view, name="delete_account"),
]
