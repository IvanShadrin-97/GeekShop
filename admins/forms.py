from django import forms

from users.forms import UserRegisterForms, UserProfileForm
from users.models import User


class AdminUserCreationForm(UserRegisterForms):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image')


class AdminUserUpdateForm(UserProfileForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'readonly': False}))
