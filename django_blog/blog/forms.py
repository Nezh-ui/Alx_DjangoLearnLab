from xml.etree.ElementTree import Comment
from django import forms    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Profile

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

class PostForm(forms.ModelForm): # Post form
    tags = forms.CharField(max_length=100, required=False) # Tags field
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
                    'content': forms.Textarea(attrs={'rows': 5}),
                    'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
                }
    
        def clean_title(self):
            title = self.cleaned_data.get('title')  # type: ignore
            if not title:
                raise forms.ValidationError("Title is required.")
            return title

class CommentForm(forms.ModelForm): # Comment form
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')  # type: ignore
        if not content:
            raise forms.ValidationError("Content is required.")
        return content