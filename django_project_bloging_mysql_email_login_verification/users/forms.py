from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q

from users.models import Profile
from .models import PendingUser




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered. Please use a different one.")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username or Email"
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username or Email'
    def clean(self):
        username = self.cleaned_data.get('username')
        if PendingUser.objects.filter(Q(username=username) | Q(email=username)).exists():
            raise forms.ValidationError("Your account is not verified. Please check your email.")
        return super().clean()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']