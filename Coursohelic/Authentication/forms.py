from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required') 
    class Meta:
        model= User
        fields = ['first_name', 'institution']