import pytest
from user.models import Profile
from user.models import User
from .fixtures import UserFactory, email_confirmation


@pytest.mark.django_db
class TestUserModel:

    def test_whether_profile_is_created(self):
        user = UserFactory()
        email_confirmation(user)
        profile, created = Profile.objects.get_or_create(user)
        assert profile.user.first_name == "reza"
        assert profile.user.last_name == "shakeri"
        assert profile.user.username == "rzashakeri"
        assert profile.user.email == "rezashakeri@test.com"
        assert profile.user.is_active
        assert profile.user.is_superuser is False

    def test_user_str_method_return_username(self):
        user = UserFactory(first_name="", last_name="")
        email_confirmation(user)
        assert user.__str__() == "rzashakeri"


@pytest.mark.django_db
class TestProfileModel:

    def test_profile_str_method_return_true_username(self):
        user = UserFactory()
        email_confirmation(user)
        assert user.profile.__str__() == "rzashakeri"

    def test_profile_get_absolute_url_method_return_true_address(
            self, client
    ):
        user = UserFactory()
        email_confirmation(user)
        client.force_login(user)
        response = client.get(user.profile.get_absolute_url())
        assert user.profile.get_absolute_url
        assert response.status_code == 200
