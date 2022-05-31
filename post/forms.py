from django import forms

from post.models import Post


class UploadPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["caption", "content"]
        widgets = {
            "caption": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered w-full",
                    "placeholder": "Create a Post",
                    "rows": "4",
                }
            ),
            "content": forms.FileInput(attrs={"class": ""}),
        }
