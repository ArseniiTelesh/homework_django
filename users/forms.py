from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ResetPasswordForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)


class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "phone", "country", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()