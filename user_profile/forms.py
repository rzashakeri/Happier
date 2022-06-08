import datetime

from django import forms

from user_management.models import User
from user_profile.models import Profile


class EditPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "mt-1 input input-bordered w-full max-w-xs",
                    "placeholder": "First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "mt-1 input input-bordered w-full max-w-xs",
                    "placeholder": "Last Name",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "mt-1 input input-bordered w-full max-w-xs",
                    "placeholder": "Email",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "mt-1 input input-bordered w-full max-w-xs",
                    "placeholder": "Username",
                }
            ),
            "biography": forms.Textarea(
                attrs={
                    "class": "resize-none mt-1 textarea textarea-bordered bg-base-100 text-base-content",
                    "placeholder": "bio",
                    "cols": "50",
                    "rows": "5",
                }
            ),
            "profile_image": forms.FileInput(attrs={"class": ""}),
        }
        error_messages = {
            "email": {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        labels = {"email": "Email"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].disabled = True


class EditProfileForm(forms.ModelForm):
    class Meta:
        year = datetime.date.today().year
        model = Profile
        fields = ["profile_image", "birthday", "biography"]
        widgets = {
            "biography": forms.Textarea(
                attrs={
                    "class": "resize-none mt-1 textarea textarea-bordered bg-base-100 text-base-content",
                    "placeholder": "bio",
                    "cols": "50",
                    "rows": "5",
                }
            ),
            "profile_image": forms.FileInput(attrs={"class": ""}),
            "birthday": forms.SelectDateWidget(years=range(1950, year)),
        }
