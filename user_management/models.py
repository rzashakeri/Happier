from birthday import BirthdayField, BirthdayManager
from constrainedfilefield.fields import ConstrainedImageField
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# custom user model
class User(AbstractUser):
    phone_number = PhoneNumberField(blank=True)
    profile_image = ConstrainedImageField(
        upload_to="profile",
        null=True,
        blank=True,
        content_types=["image/png", "image/jpeg"],
        max_upload_size=10485760,
    )
    biography = models.CharField(max_length=200, null=True, blank=True)
    birthday = BirthdayField()
    objects = BirthdayManager()

    # show user data in admin when UserAdmin class in admin not set
    def __str__(self):
        if self.get_full_name() != "":
            return self.get_full_name()
        return self.username

    # metadata about user in admin
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
