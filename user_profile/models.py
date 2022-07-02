import uuid

from birthday import BirthdayField, BirthdayManager
from constrainedfilefield.fields import ConstrainedImageField
from django.db import models
from django.urls import reverse

from user_management.models import User


def user_directory_path(instance, filename):
    filename, extension = filename.split(".")
    if extension in ["png", "jpeg", "heic", "heif", "jpg"]:
        return "profile/image/{0}.{1}".format(str(uuid.uuid4().hex), extension)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", symmetrical=False, related_name="followed_by", blank=True
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

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile", kwargs={"username": self.user.username})
