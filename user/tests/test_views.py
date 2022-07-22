import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects
from .fixtures import (
    user,
    user_without_full_name,
    uploaded_file,
    edit_profile_data,
    edit_profile_image,
    path_of_test_files_directory,
)
from ..forms import EditProfileForm
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
from birthday import BirthdayField, BirthdayManager


@pytest.mark.django_db
class TestProfileView:
    def test_profile_view_when_user_is_authenticated_return_correct_profile(
            self, user, client
    ):
        client.force_login(user)  # user logged in
        response = client.get(user.profile.get_absolute_url())
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert (
                '<h1 class="text-3xl md:text-4xl font-semibold">Test_first_name test_last_name</h1>'
                in str(content)
        )
        response = client.get("/user_not_exist", follow=True)
        assert response.status_code == 404

        response = client.post("/accounts/logout/")
        assert response.status_code == 302

    def test_profile_view_when_user_is_anonymous_return_login_page(self, user, client):
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
    def test_does_the_profile_editing_page_load_correctly(self, user, client):
        client.force_login(user)
        response = client.get(reverse("edit_profile"))
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert response.wsgi_request.path == "/accounts/edit/profile"
        assert '<div class="label-text mb-1">Biography</div>' in str(content)

    def test_edit_profile_form_is_valid(
            self, user, edit_profile_image, edit_profile_data
    ):
        edit_profile_form = EditProfileForm(
            data=edit_profile_data,
            instance=user.profile,
            files=edit_profile_image,
        )
        assert edit_profile_form.is_valid()

    def test_posted_edit_profile_form_data(self, user, edit_profile_data, client):
        client.force_login(user)
        response = client.post(reverse("edit_profile"), edit_profile_data)
        content = response.content.decode(response.charset)
        assert response.status_code == 200
        assert response.resolver_match.url_name == 'edit_profile'
        assert response.resolver_match.view_name == 'edit_profile'
        assert response.request['PATH_INFO'] == reverse("edit_profile")
        assert '<input type="text" name="job" value="Software Engineer" class="input input-bordered w-full mt-1" placeholder="Job" maxlength="20" id="id_job">' in str(content)
        

