import datetime

from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
    AddEmailForm,
    ChangePasswordForm,
    SetPasswordForm,
)
from constrainedfilefield.fields import ConstrainedImageField, ConstrainedFileField
from crispy_forms.helper import FormHelper
from django import forms
from django.forms import SelectDateWidget

from user.models import User
from utility.generator import user_directory_path
from user.models import Profile
from user.tests.fixtures import profile_image
from user.views import edit_personal_information

class_list = "block w-full mt-2 input input-bordered w-full max-w-xs"
edit_personal_information_form_class_list = "mt-1 input input-bordered w-full max-w-xs"
change_password_form_class_list = "input input-bordered w-full my-3"


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs[
            "class"
        ] = class_list
        self.fields["email"].widget.attrs[
            "class"
        ] = class_list
        self.fields["password1"].widget.attrs[
            "class"
        ] = class_list


class CustomSigninForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs[
            "class"
        ] = class_list
        self.fields["password"].widget.attrs[
            "class"
        ] = class_list
        self.helper = FormHelper(self)


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs[
            "class"
        ] = "block w-32 input input-bordered max-w-xs"


class CustomResetPasswordFromKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs[
            "class"
        ] = class_list
        self.fields["password2"].widget.attrs[
            "class"
        ] = class_list


class CustomAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs[
            "class"
        ] = "input input-bordered w-full max-w-xs mt-2"


class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["oldpassword"].widget.attrs[
            "class"
        ] = change_password_form_class_list
        self.fields["password1"].widget.attrs[
            "class"
        ] = change_password_form_class_list
        self.fields["password2"].widget.attrs[
            "class"
        ] = change_password_form_class_list


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
                    "class": edit_personal_information_form_class_list ,
                    "placeholder": "First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": edit_personal_information_form_class_list,
                    "placeholder": "Last Name",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": edit_personal_information_form_class_list,
                    "placeholder": "Email",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "mt-1 input input-bordered w-full max-w-xs",
                    "placeholder": "Username",
                    "minlength": "5",
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
        fields = ["profile_image", "birthday", "biography", "job", "is_private"]
        widgets = {
            "biography": forms.Textarea(
                attrs={
                    "class": "resize-none mt-1 textarea textarea-bordered bg-base-100 text-base-content",
                    "placeholder": "bio",
                    "cols": "50",
                    "rows": "5",
                }
            ),
            "profile_image": forms.FileInput(attrs={"class": "pond"}),
            "birthday": forms.SelectDateWidget(years=range(1950, year)),
            "job": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full mt-1",
                    "placeholder": "Job",
                }
            ),
            "is_private": forms.CheckboxInput(attrs={"class": "toggle toggle-accent"}),
        }


# getting user information in seperated forms


class FullNameForm(forms.Form):
    class_value = "input input-bordered w-full my-2"
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": class_value, "id": "first_name", "placeholder": "What Is Your Name ?"}),
        required=False,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": class_value, "id": "last_name", "placeholder": "What Is Last Name ?"}),
        required=False,
    )


class BiographyForm(forms.Form):
    biography = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={"class": "textarea textarea-bordered my-2", "rows": "5", "placeholder": "Tell about yourself in 200 characters"}
        ),
        required=False,
    )


class BirthdayForm(forms.Form):
    year = datetime.date.today().year
    birthday = forms.DateField(
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
            years=range(1950, year),
            attrs={"style": "background-color:#ededed;border-radius: 5px;"},
        ),
        required=False,
    )


class JobForm(forms.Form):
    job = forms.CharField(
        widget=forms.TextInput(attrs={"class": "input input-bordered w-full my-2",  "placeholder": "What Is Your Job ?"}),
        required=False,
    )


class UploadProfileImageForm(forms.Form):
    profile_image = ConstrainedImageField(
        upload_to=user_directory_path,
        null=True,
        blank=True,
        content_types=["image/png", "image/jpeg"],
        max_upload_size=10485760,
    ).formfield(
        widget=forms.FileInput(
            attrs={
                "class": "w-[100px] max-2sm:flex max-2sm:flex-col",
                "onchange": "loadFile(event)"
            }
        )
    )
