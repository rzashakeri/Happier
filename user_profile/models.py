from django.db import models

from user_management.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)

    def __str__(self):
        return self.user.username
