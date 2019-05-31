from django import forms
from django.contrib.auth.models import User
from .models import Tests, Questions, Variant


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'type': "text", 'id': "inputEmail", 'class': "form-control", 'placeholder': "Login"}),
            'password': forms.TextInput(attrs={'type': "password", 'id': "inputPassword", 'class': "form-control", 'placeholder': "Password"}),
        }


class AddTestForm(forms.ModelForm):

    class Meta:
        model = Tests
        fields = ('name', 'description', 'sum')


class AddQuestionsForm(forms.ModelForm):

    class Meta:
        model = Questions
        fields = ('test', 'title', 'text', 'index')


class AddAnswerForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = ('questions', 'title', 'correct')
