from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'slug', 'price', 'description', 'image', 'author', 'genre']

    def clean(self):
        slug = self.cleaned_data.get('title').lower().replace(' ', '-')
        if Book.objects.filter(slug=slug).exists():
            raise forms.ValidationError('Book with such title already exists!')
        return self.cleaned_data


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        template_name = 'book/register.html'
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        template_name = 'book/login.html'
        fields = ['username', 'password1']
