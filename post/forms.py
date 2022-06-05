from django import forms

from post.models import Post, PostAttachment


class UploadPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption"]
        widgets = {
            "caption": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered w-full",
                    "placeholder": "Create a Post",
                    "rows": "4",
                }
            )
        }


class UploadPostAttachmentForm(forms.ModelForm):
    class Meta:
        model = PostAttachment
        fields = ["image", "audio", "video"]
        widgets = {
            "audio": forms.FileInput(attrs={"accept": "audio/*"}),
            "video": forms.FileInput(attrs={"accept": "video/*"}),
            "image": forms.FileInput(attrs={"accept": "image/*"}),
        }
