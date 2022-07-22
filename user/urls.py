from django.urls import path

from user.views import (
    profile_view,
    edit_profile_view,
    delete_account_view,
    edit_personal_information,
    followers_list,
    followings_list,
    follow_request,
    follow_request_accepted,
    follow_request_declined,
    follow_request_list,
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
    path("<str:username>/followers", followers_list, name="followers"),
    path("<str:username>/following", followings_list, name="following"),
    path(
        "follow/request/<str:username>/",
        follow_request,
        name="follow_request",
    ),
    path(
        "follow/request/<str:username>/accepted",
        follow_request_accepted,
        name="follow_request_accepted",
    ),
    path(
        "follow/request/<str:username>/declined",
        follow_request_declined,
        name="follow_request_declined",
    ),
    path(
        "account/follow/requests/",
        follow_request_list,
        name="follow_request_list",
    ),
]
