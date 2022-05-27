from django import forms

from user_management.models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'biography', 'profile_image', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'mt-1 input input-bordered w-full max-w-xs',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'mt-1 input input-bordered w-full max-w-xs',
                'placeholder': 'Last Name'
            }),
            'email': forms.TextInput(attrs={
                'class': 'mt-1 input input-bordered w-full max-w-xs',
                'placeholder': 'Email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'mt-1 input input-bordered w-full max-w-xs',
                'placeholder': 'Username'
            }),
            'biography': forms.Textarea(attrs={
                'class': 'resize-none mt-1 textarea textarea-bordered',
                'placeholder': 'bio',
                'cols': '42',
                'rows': '5'
            }),
            'profile_image': forms.FileInput(attrs={
                'class': ''
            })
        }
        error_messages = {
            'email': {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].disabled = True
