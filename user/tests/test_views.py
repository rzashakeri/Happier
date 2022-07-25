import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects
from .fixtures import (
    uploaded_file,
    profile_data,
    profile_image,
    path_of_test_files_directory,
    personal_information_data,
    bad_personal_information_data,
    UserFactory,
    email_confirmation,
)
from ..forms import EditProfileForm, EditPersonalInformationForm
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
from birthday import BirthdayField, BirthdayManager
from django.core.exceptions import ObjectDoesNotExist
from actstream.models import following, followers
from actstream.actions import follow, unfollow
from ..models import User, Profile


@pytest.mark.django_db
class TestProfileView:
    def test_profile_view_when_user_is_authenticated_return_correct_profile(
            self, client
    ):
        user = UserFactory()
        email_confirmation(user)
        client.force_login(user)  # user logged in
        response = client.get(user.profile.get_absolute_url())
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert (
                '<h1 class="text-3xl md:text-4xl font-semibold">Reza shakeri</h1>'
                in str(content)
        )
        response = client.get("/user_not_exist", follow=True)
        assert response.status_code == 404

        response = client.post("/accounts/logout/")
        assert response.status_code == 302

    def test_profile_view_when_user_is_anonymous_return_login_page(self, client):
        response = client.get("/test_username/", follow=True)
        content = response.content.decode(response.charset)
        assertRedirects(response, "/accounts/login/?next=/test_username/")
        assert response.status_code == 200
        assert response.template_name[0] == "account/login.html"
        assert '<h1 class="text-3xl font-semibold text-center">Login</h1>' in str(
            content
        )
        assert response.resolver_match.url_name == "account_login"
        assert response.resolver_match.view_name == "account_login"


@pytest.mark.django_db
class TestEditProfileView:
    def test_does_the_profile_editing_page_load_correctly(self, client):
        user = UserFactory()
        email_confirmation(user)
        response = client.get(
            reverse("edit_profile")
        )  # test when user is not logged in redirecting to login page
        assert response.status_code == 302
        assert response.url == "/accounts/login/?next=" + reverse("edit_profile")
        client.force_login(user)
        response = client.get(reverse("edit_profile"))
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert response.wsgi_request.path == "/accounts/edit/profile"
        assert '<div class="label-text mb-1">Biography</div>' in str(content)

    def test_edit_profile_form_is_valid(self, profile_image, profile_data):
        user = UserFactory()
        edit_profile_form = EditProfileForm(
            data=profile_data,
            instance=user.profile,
            files=profile_image,
        )
        assert edit_profile_form.is_valid()

    def test_posted_edit_profile_form_data(self, profile_data, client):
        user = UserFactory()
        email_confirmation(user)
        client.force_login(user)
        assert user.profile.biography is None
        assert user.profile.birthday is None
        assert not user.profile.is_private
        assert user.profile.job is None
        assert user.profile.profile_image.name is None
        response = client.post(reverse("edit_profile"), profile_data)
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert response.resolver_match.url_name == "edit_profile"
        assert response.resolver_match.view_name == "edit_profile"
        assert response.request["PATH_INFO"] == reverse("edit_profile")
        assert (
                '<input type="text" name="job" value="Software Engineer" class="input input-bordered w-full mt-1" placeholder="Job" maxlength="20" id="id_job">'
                in str(content)
        )
        edited_profile = Profile.objects.get(user_id=user.pk)
        assert edited_profile.is_private
        assert edited_profile.birthday == profile_data["birthday"]
        assert edited_profile.biography == profile_data["biography"]
        assert edited_profile.job == profile_data["job"]
        assert edited_profile.profile_image.name


@pytest.mark.django_db
class TestEditPersonalInformationView:
    def test_dose_edit_personal_information_page_load_correctly(self, client):
        user = UserFactory()
        email_confirmation(user)
        response = client.get(reverse("edit_personal_information"))
        assert response.status_code == 302  # redirect to login page
        assert response.url == "/accounts/login/?next=" + reverse(
            "edit_personal_information"
        )
        client.force_login(user)
        response = client.get(reverse("edit_personal_information"))
        assert response.status_code == 200
        assert response.request["PATH_INFO"] == reverse("edit_personal_information")
        assert response.resolver_match.url_name == "edit_personal_information"
        assert response.resolver_match.view_name == "edit_personal_information"

    def test_edit_personal_information_form_is_valid(self, personal_information_data):
        user = UserFactory()
        email_confirmation(user)
        edit_personal_information_form = EditPersonalInformationForm(
            data=personal_information_data, instance=user
        )
        assert edit_personal_information_form.is_valid()

    def test_edit_personal_information_is_not_valid(
            self, bad_personal_information_data
    ):
        user = UserFactory()
        email_confirmation(user)
        edit_personal_information_form: EditPersonalInformationForm = (
            EditPersonalInformationForm(data=bad_personal_information_data)
        )
        assert not edit_personal_information_form.is_valid()

    def test_posted_edit_personal_information_data(
            self, personal_information_data, client
    ):
        user = UserFactory()
        email_confirmation(user)
        client.force_login(user)
        response = client.post(
            reverse("edit_personal_information"), data=personal_information_data
        )
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert (
                '<input type="text" name="username" value="rzashakeri" class="mt-1 input input-bordered w-full max-w-xs" placeholder="Username" minlength="5" maxlength="150" required id="id_username">'
                in str(content)
        )
        assert response.request["PATH_INFO"] == "/accounts/edit/personal-information"
        assert response.wsgi_request.user.username == "rzashakeri"

        edited_user = User.objects.get(pk=user.pk)
        assert edited_user.username == "rzashakeri"
        assert edited_user.first_name == "reza"
        assert edited_user.last_name == "shakeri"


@pytest.mark.django_db
class TestDeleteAccountView:
    def test_delete_account_is_successful(self, client):
        user = UserFactory()
        email_confirmation(user)
        client.force_login(user)
        response = client.post(
            reverse("delete_account"), data={"delete": "yes"}, follow=True
        )
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert response.request["PATH_INFO"] == reverse("home")
        assert (
                '<p class="mx-3">Your account has been successfully deleted, We hope you will be back soon :)</p>'
                in str(content)
        )
        try:
            User.objects.get(pk=user.pk)
        except ObjectDoesNotExist:
            assert True

    def test_user_cancelled_delete_account(self, client):
        user = UserFactory()
        email_confirmation(user)
        client.force_login(user)
        response = client.post(
            reverse("delete_account"), data={"delete": "no"}, follow=True
        )
        assert response.status_code == 200
        assert response.request["PATH_INFO"] == reverse("feed")

    def test_get_delete_account_page(self, client):
        user = UserFactory()
        email_confirmation(user)
        client.force_login(user)
        response = client.get(reverse("delete_account"))
        assert response.status_code == 200


@pytest.mark.django_db
class TestFollowRequestView:
    def test_followed_public_account(self, client):
        current_user = UserFactory()
        email_confirmation(current_user)
        user_we_want_to_follow = UserFactory(
            first_name="John",
            last_name="Smith",
            username="JohnSmith",
            email="JohnSmith@test.com",
        )
        email_confirmation(user_we_want_to_follow)
        client.force_login(current_user)
        response = client.post(reverse("follow_request", kwargs={"username": user_we_want_to_follow.username}))
        assert response.status_code == 200
        assert response.content == b'{"status": "followed"}'

    def test_unfollowed_public_account(self, client):
        current_user = UserFactory()
        email_confirmation(current_user)
        user_we_want_to_unfollow = UserFactory(
            first_name="John",
            last_name="Smith",
            username="JohnSmith",
            email="JohnSmith@test.com",
        )
        email_confirmation(user_we_want_to_unfollow)
        follow(current_user, user_we_want_to_unfollow)
        client.force_login(current_user)
        response = client.post(reverse("follow_request", kwargs={"username": user_we_want_to_unfollow.username}))
        assert response.status_code == 200
        assert response.content == b'{"status": "unfollow"}'
        assert response.request["PATH_INFO"] == reverse("follow_request", kwargs={"username":user_we_want_to_unfollow.username})
