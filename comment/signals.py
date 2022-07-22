from django.db.models.signals import post_save
from actstream import action
from django.dispatch import receiver
from comment.models import Comment


def created_comment(sender, instance, created, **kwargs):
    """
    if user commented on the post this signal has been run
    and created an activity with verb and object
    Example: reza commented example text on post
    """
    if created:
        action.send(
            instance.user,
            verb="commented",
            action_object=instance,
            target=instance.post,
        )


post_save.connect(created_comment, sender=Comment)
