from django.db.models.signals import post_save
from django.dispatch import receiver
from actstream.actions import follow, unfollow
from user.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        follow(instance, instance)
