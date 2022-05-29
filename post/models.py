import uuid

from constrainedfilefield.fields import ConstrainedFileField
from django.db import models

from user_management.models import User


def user_directory_path(instance, filename):
    filename, extension = filename.split('.')
    return 'post/{0}.{1}'.format(str(uuid.uuid4()), extension)


class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    parent = models.ForeignKey('PostComment', on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f'{self.user} : {self.comment_text}'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = ConstrainedFileField(upload_to=user_directory_path, unique=True, null=True, blank=True, content_types=['image/png', 'image/jpeg', 'image/heic', 'image/heif', 'video/mp4', 'video/quicktime'])
    caption = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('PostCategory')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.user} / {self.created_at}'


class PostCategory(models.Model):
    title = models.CharField(max_length=30)
    url_title = models.SlugField(max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
