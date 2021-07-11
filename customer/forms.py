from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "user_name", "password1", "password2"]
        widgets = {'first_name': forms.TextInput(attrs={'class': "form-control p-2"}),
                   'last_name': forms.TextInput(attrs={'class': "form-control p-2"}),
                   'email': forms.EmailInput(attrs={'class': "form-control p-2"}),
                   'user_name': forms.TextInput(attrs={'class': "form-control p-2"}),
                   'password1': forms.PasswordInput(attrs={'class': "form-control p-2"}),
                   'password2': forms.PasswordInput(attrs={'class': "form-control p-2"}),

                   }
class LoginForm(forms.Form):
    username=forms.CharField(widgets=forms.TextInput(attrs={'class': "form-control p-2"}))
    password = forms.CharField(widgets=forms.PasswordInput(attrs={'class': "form-control p-2"}))
