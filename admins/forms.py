from django import forms

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username','image', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'forms-control py-4', 'readonly': False}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forms-control py-4', 'readonly': False}))
