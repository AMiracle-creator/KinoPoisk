from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import KinopoiskUser


class RegForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # password = forms.CharField(label='Password', required=True)
    # sec_password = forms.CharField(label='Repeat password', required=True)

    class Meta:
        model = KinopoiskUser
        fields = ['email', 'password1', 'password2']


class AuthForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password')


class EditProfForm(forms.ModelForm):
     class Meta:
         model = KinopoiskUser
         fields = ['name', 'img', 'email']

