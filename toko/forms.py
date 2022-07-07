from django.contrib.auth.forms import UserCreationForm

from toko.models.user import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Repeat password'}))
    terms = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input me-2', 'type':'checkbox', 'placeholder': 'EULA'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'terms')
        