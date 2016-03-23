from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'type': "text", 'id': "inputEmail", 'class': "form-control", 'placeholder': "Login"}),
            'password': forms.TextInput(attrs={'type': "password", 'id': "inputPassword", 'class': "form-control", 'placeholder': "Password"}),
        }
