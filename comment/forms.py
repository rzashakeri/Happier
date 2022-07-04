from django import forms

from comment.models import Comment


class CreateCommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.TextInput(
                attrs={
                    "class": "px-3 py-3 w-full h-11 bg-base-200 rounded-lg placeholder:text-slate-600 font-medium",
                    "placeholder": "Write a comment",
                    "id": "comment-text",
                }
            )
        }
