from django import forms    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_blog.blog.models import Profile

class CustomUserCreationForm(UserCreationForm): # User registration form
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomProfileUpdateForm(forms.ModelForm): # Profile update form
    class Meta:
        model = Profile
        fields = ['bio', 'profile_photo']

class CustomUserUpdateForm(forms.ModelForm): # User update form
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']