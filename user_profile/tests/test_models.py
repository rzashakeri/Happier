import pytest

from user_management.models import User
from user_profile.models import Profile
from utility.generator import user_directory_path


@pytest.mark.django_db
class TestUserProfile:
    def test_create_profile(self):
        user, created = User.objects.get_or_create(
            first_name="test_first_name",
            last_name="test_last_name",
            username="test_username",
            email="test@test.com",
            is_active=True,
            is_superuser=False,
        )
        profile, created = Profile.objects.get_or_create(user)
        assert profile.user.first_name == "test_first_name"
        assert profile.user.last_name == "test_last_name"
        assert profile.user.username == "test_username"
        assert profile.user.email == "test@test.com"
        assert profile.user.is_active
        assert profile.user.is_superuser is False

    def test_user_directory_path(self):
        user, created = User.objects.get_or_create(
            first_name="test_first_name",
            last_name="test_last_name",
            username="test_username",
            email="test@test.com",
            is_active=True,
            is_superuser=False,
        )
        profile, created = Profile.objects.get_or_create(user)

        mp4_file = user_directory_path(profile, "file.mp4")
        mp3_file = user_directory_path(profile, "file.mp3")
        png_file = user_directory_path(profile, "file.png")
        jpeg_file = user_directory_path(profile, "file.jpeg")
        heic_file = user_directory_path(profile, "file.heic")
        heif_file = user_directory_path(profile, "file.heif")
        jpg_file = user_directory_path(profile, "file.jpg")
        bad_file = user_directory_path(profile, "file.bad")

        files = [
            mp4_file,
            mp3_file,
            png_file,
            jpeg_file,
            heic_file,
            heif_file,
            jpg_file,
        ]

        assert all(files)
        assert not bad_file
