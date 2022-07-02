from django import forms

from comment.models import Comment


class CreateCommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.TextInput(
                attrs={
                    "class": "pt-2 pb-2 pl-3 w-full h-11 bg-slate-100 rounded-lg placeholder:text-slate-600 font-medium pr-20",
                    "placeholder": "Write a comment",
                    "id": "comment-text",
                }
            )
        }
