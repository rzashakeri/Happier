import pytest
from django.urls import reverse
from allauth.account.forms import EmailAwarePasswordResetTokenGenerator
from allauth.account.utils import user_pk_to_url_str

from user.models import User
from user.tests.fixtures import UserFactory, email_confirmation


@pytest.mark.django_db
def test_return_correct_widget_attrs_signup_form(client):
    response = client.get(reverse("account_signup"))
    content = response.content.decode(response.charset)
    assert (
            'block w-full mt-2 input input-bordered w-full max-w-xs'
            in str(content)
    )


@pytest.mark.django_db
def test_return_correct_widget_attrs_reset_password_form(client):
    response = client.get(reverse("account_reset_password"))
    content = response.content.decode(response.charset)
    assert (
            'block w-32 input input-bordered max-w-xs'
            in str(content)
    )


@pytest.mark.django_db
def test_return_correct_widget_attrs_reset_password_from_key_form(client):
    current_user = UserFactory()
    email_confirmation(current_user)
    token_generator = EmailAwarePasswordResetTokenGenerator()
    user = User.objects.get(email=current_user.email)
    temp_key = token_generator.make_token(user)
    response = client.get(reverse("account_reset_password_from_key", kwargs=dict(uidb36=user_pk_to_url_str(user), key=temp_key)), follow=True)
    content = response.content.decode(response.charset)
    assert (
            'block w-full mt-2 input input-bordered w-full max-w-xs'
            in str(content)
    )


@pytest.mark.django_db
def test_return_correct_widget_attrs_add_email_form(client):
    current_user = UserFactory()
    email_confirmation(current_user)
    client.force_login(current_user)
    response = client.get(reverse("account_email"))
    content = response.content.decode(response.charset)
    assert (
            'input input-bordered w-full max-w-xs mt-2'
            in str(content)
    )


@pytest.mark.django_db
def test_return_correct_widget_attrs_change_password_form(client):
    current_user = UserFactory()
    email_confirmation(current_user)
    client.force_login(current_user)
    response = client.get(reverse("account_change_password"))
    content = response.content.decode(response.charset)
    assert (
            'input input-bordered w-full my-3'
            in str(content)
    )

