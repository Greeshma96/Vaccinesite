
from django import forms
from django.forms import ModelForm
from .models import Register

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    class Meta:
        model = Register
        fields = ["username", "password"]