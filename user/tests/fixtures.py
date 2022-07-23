import pytest

from user.forms import EditPersonalInformationForm
from user.models import Profile
from user.models import User
from user.models import User, Profile
from django.contrib import auth
from allauth.account.models import EmailAddress
import os
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
from birthday import BirthdayField, BirthdayManager


@pytest.fixture
def user():
    user, created = User.objects.get_or_create(  # created user
        username="test_username",
        first_name="test_first_name",
        last_name="test_last_name",
        email="test@test.com",
        is_active=True,
        is_superuser=False,
    )

    (
        user_email_address,
        created,
    ) = EmailAddress.objects.get_or_create(  # user email confirmation
        email=user.email, user=user, verified=True, primary=True
    )

    return user


@pytest.fixture
def user_without_full_name():
    user, created = User.objects.get_or_create(
        username="test_username",
        email="test@test.com",
        is_active=True,
        is_superuser=False,
    )
    return user


@pytest.fixture
def path_of_test_files_directory():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    test_files_directory = os.path.join(current_directory, "test_files", "avatar.png")
    return test_files_directory


@pytest.fixture
def profile_image(path_of_test_files_directory):
    uploaded_file = File(open(path_of_test_files_directory, "rb"))
    file_data = {
        "uploaded_file": SimpleUploadedFile(
            name=uploaded_file.name,
            content=open(path_of_test_files_directory, "rb").read(),
            content_type="image/png",
        )
    }
    return file_data


@pytest.fixture
def uploaded_file(path_of_test_files_directory):
    uploaded_file = File(open(path_of_test_files_directory, "rb"))
    return uploaded_file


@pytest.fixture
def profile_data(uploaded_file):
    user_birthday = datetime(2010, 1, 1).date()
    form_data = {
        "profile_image": uploaded_file,
        "birthday": user_birthday,
        "biography": "test_biography",
        "job": "Software Engineer",
        "is_private": True,
    }
    return form_data


@pytest.fixture
def personal_information_data():
    edit_personal_information_data = {
        "first_name": "reza",
        "last_name": "shakeri",
        "username": "rzashakeri"
    }

    return edit_personal_information_data


@pytest.fixture
def bad_personal_information_data():
    edit_personal_information_data = {
        "first_name": "reza",
        "last_name": "shakeri",
        "username": "rza"
    }

    return edit_personal_information_data
