from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import Todo



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'
    }))


class UserTodoForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите заголовок'
    }))
    memo = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'style': 'height: 105px;'
    }))
    important = forms.BooleanField(required=False)

    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
