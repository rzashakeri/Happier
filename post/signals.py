from django.db.models.signals import post_save
from actstream import action
from django.dispatch import receiver

from comment.models import Comment
from post.models import Post, PostLike


@receiver(post_save, sender=Post)
def created_post(sender, instance, created, **kwargs):
    """
    if post has been created this signal is run
    and by using the action method in actstream created an activity with verb and object
    Example: reza upload new post
    """
    if created:
        action.send(instance.user, verb="upload new post", action_object=instance)


@receiver(post_save, sender=PostLike)
def created_like(sender, instance, created, **kwargs):
    """
    if user liked a post this signal has been run and created an activity with verb and object
    Example: reza liked example post
    """
    if created:
        action.send(
            instance.user, verb="liked", action_object=instance, target=instance.post
        )
