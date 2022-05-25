from django.contrib.auth.models import AbstractUser
from django.db import models


# custom user model
class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile', null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)

    # show user data in admin when UserAdmin class in admin not set
    def __str__(self):
        if self.get_full_name() != '':
            return self.get_full_name()
        return self.username

    # metadata about user in admin
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
