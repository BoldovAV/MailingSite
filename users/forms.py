from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from newsletter.forms import StyleForMixin
from users.models import User


class UserRegisterForm(StyleForMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name',)


class UserForm(StyleForMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
