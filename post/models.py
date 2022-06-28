import audio_metadata
from audio_metadata.utils import humanize_duration
from audio_validator.validator import AudioValidator
from constrainedfilefield.fields import ConstrainedFileField, ConstrainedImageField
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.db import models
from django_comments.abstracts import CommentAbstractModel, BaseCommentAbstractModel
from tbm_utils import humanize_filesize

from user_management.models import User
from utility.generator import hex_uuid, user_directory_path


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField("PostCategory", blank=True)
    caption = models.CharField(max_length=2000)
    slug = models.SlugField(default=hex_uuid, editable=False)
    image = models.ForeignKey("Image", on_delete=models.CASCADE, null=True, blank=True)
    audio = models.ForeignKey("Audio", on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey("Video", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.caption[:9])


class Image(models.Model):
    file = ConstrainedImageField(
        upload_to=user_directory_path,
        content_types=["image/png", "image/jpeg", "image/heic", "image/heif"],
        blank=True,
    )


class Video(models.Model):
    file = ConstrainedFileField(
        upload_to=user_directory_path, content_types=["video/mp4"], blank=True
    )


class Audio(models.Model):
    file = models.FileField(
        upload_to=user_directory_path,
        blank=True,
        validators=[AudioValidator("mp3")],
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    artist = models.CharField(max_length=100, null=True, blank=True)
    album = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    data = models.CharField(max_length=30, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        file = self.file.file
        file_path = TemporaryUploadedFile.temporary_file_path(file)
        metadata = audio_metadata.load(file_path)
        try:
            name = metadata.tags.title[0]
            self.name = name
        except AttributeError:
            pass

        try:
            artist = metadata.tags.artist[0]
            self.artist = artist
        except AttributeError:
            pass

        try:
            album = metadata.tags.album[0]
            self.album = album
        except AttributeError:
            pass

        try:
            size = metadata.filesize
            self.size = humanize_filesize(size)
        except AttributeError:
            pass

        try:
            data = metadata.tags.data[0]
            self.data = data
        except AttributeError:
            pass

        try:
            duration = metadata.streaminfo["duration"]
            self.duration = humanize_duration(duration)
        except AttributeError:
            pass

        super(Audio, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} likes {self.post}"


class PostCategory(models.Model):
    title = models.CharField(max_length=30)
    url_title = models.SlugField(max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
