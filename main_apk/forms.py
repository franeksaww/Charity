from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):
    email = forms.CharField(label="email",
                            widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="password1",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class RegisterForm(forms.Form):
    email = forms.CharField(label="email",
                            widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="password1",
                                widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(label="password1",
                               widget=forms.PasswordInput(attrs={'placeholder': 'Powtóz hasło'}))


class ChangePasswordForm(forms.Form):
    email = forms.CharField(label="email",
                            widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    email2 = forms.CharField(label="email2",
                                widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    def clean(self):
        cleaned_data = super().clean()
        email1 = cleaned_data.get('email')
        email2 = cleaned_data.get('email2')
        if email1 != email2:
            raise forms.ValidationError('Hasła nie są podobne')