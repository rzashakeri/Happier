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
from crispy_forms.helper import FormHelper
from django import forms

from user.models import User
from .models import Profile


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.fields["email"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.fields["password1"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"


# Signup Form in Separate Step
class SignupFormStepOne(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name")


class SignupFormStepTwo(forms.Form):
    last_name = forms.CharField(max_length=30, label="Lirst Name")


class SignupFormStepThree(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.fields.pop("email")
        self.fields.pop("password1")
        self.fields.pop("password2")


class SignupFormStepFour(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.fields.pop("username")
        self.fields.pop("password1")
        self.fields.pop("password2")


class SignupFormStepFive(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.fields["password2"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.fields.pop("username")
        self.fields.pop("email")


class CustomSigninForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.fields["password"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
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
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.fields["password2"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"


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
        ] = "input input-bordered w-full my-3"
        self.fields["password1"].widget.attrs[
            "class"
        ] = "input input-bordered w-full my-3"
        self.fields["password2"].widget.attrs[
            "class"
        ] = "input input-bordered w-full my-3"


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[""].widget.attrs[
            "class"
        ] = "input input-bordered w-full max-w-xs my-3"
        self.fields["password1"].widget.attrs[
            "class"
        ] = "input input-bordered w-full max-w-xs my-3"
        self.fields["password2"].widget.attrs[
            "class"
        ] = "input input-bordered w-full max-w-xs my-3"


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
            "profile_image": forms.FileInput(attrs={"class": ""}),
            "birthday": forms.SelectDateWidget(years=range(1950, year)),
            "job": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full mt-1",
                    "placeholder": "Job",
                }
            ),
            "is_private": forms.CheckboxInput(attrs={"class": "toggle toggle-accent"}),
        }
