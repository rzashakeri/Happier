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
        self.fields["password2"].widget.attrs[
            "class"
        ] = "block w-full mt-2 input input-bordered w-full max-w-xs"
        self.helper = FormHelper(self)


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
