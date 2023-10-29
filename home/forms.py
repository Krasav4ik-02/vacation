from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={
            'class': 'form-control',
            'style': "width: 200px",
        }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width: 200px",
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width: 200px",
            }),
        }
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width: 200px",
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width: 200px",
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width: 200px",
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': "width: 200px",
            }),
        }
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)