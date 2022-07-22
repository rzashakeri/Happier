import pytest
from user.models import Profile
from user.models import User
from .fixtures import user, user_without_full_name


@pytest.mark.django_db
class TestUserModel:

    def test_whether_profile_is_created(self, user):
        profile, created = Profile.objects.get_or_create(user)
        assert profile.user.first_name == "test_first_name"
        assert profile.user.last_name == "test_last_name"
        assert profile.user.username == "test_username"
        assert profile.user.email == "test@test.com"
        assert profile.user.is_active
        assert profile.user.is_superuser is False

    def test_user_str_method_return_username(self, user_without_full_name):
        assert user_without_full_name.__str__() == "test_username"


@pytest.mark.django_db
class TestProfileModel:

    def test_profile_str_method_return_true_username(self, user):
        assert user.profile.__str__() == "test_username"

    def test_profile_get_absolute_url_method_return_true_address(
            self, user, client
    ):
        client.force_login(user)
        response = client.get(user.profile.get_absolute_url())
        assert user.profile.get_absolute_url
        assert response.status_code == 200
