from django import forms


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