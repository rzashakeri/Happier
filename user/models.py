from birthday import BirthdayField, BirthdayManager
from constrainedfilefield.fields import ConstrainedImageField
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from utility.generator import user_directory_path


# custom user model
class User(AbstractUser):
    phone_number = PhoneNumberField(blank=True)

    # show user data in admin when UserAdmin class in admin not set
    def __str__(self):
        if self.get_full_name() != "":
            return self.get_full_name()
        return self.username

    # metadata about user in admin
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def clean(self):
        if len(self.username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follow_requests = models.ManyToManyField(
        "self", symmetrical=False, related_name="follow_request_by", blank=True
    )
    birthday = BirthdayField(blank=True, null=True)
    objects = BirthdayManager()
    profile_image = ConstrainedImageField(
        upload_to=user_directory_path,
        null=True,
        blank=True,
        content_types=["image/png", "image/jpeg"],
        max_upload_size=10485760,
    )
    profile_cover = ConstrainedImageField(
        upload_to="cover",
        null=True,
        blank=True,
        content_types=["image/png", "image/jpeg"],
        max_upload_size=10485760,
    )
    biography = models.CharField(max_length=200, null=True, blank=True)
    job = models.CharField(max_length=20, null=True, blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile", kwargs={"username": self.user.username})
