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
        ] = "input input-bordered w-full max-w-xs my-3"
        self.fields["password1"].widget.attrs[
            "class"
        ] = "input input-bordered w-full max-w-xs my-3"
        self.fields["password2"].widget.attrs[
            "class"
        ] = "input input-bordered w-full max-w-xs my-3"


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
