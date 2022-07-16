import pytest

from user.models import Profile
from user.models import User


@pytest.mark.django_db
class TestUserProfile:
    @pytest.fixture
    def user(self):
        user, created = User.objects.get_or_create(
            first_name="test_first_name",
            last_name="test_last_name",
            username="test_username",
            email="test@test.com",
            is_active=True,
            is_superuser=False,
        )
        return user

    def test_whether_profile_is_created(self, user):
        profile, created = Profile.objects.get_or_create(user)
        assert profile.user.first_name == "test_first_name"
        assert profile.user.last_name == "test_last_name"
        assert profile.user.username == "test_username"
        assert profile.user.email == "test@test.com"
        assert profile.user.is_active
        assert profile.user.is_superuser is False
