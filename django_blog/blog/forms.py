from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post
from django.conf import settings

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
#Edit basic user info
class UserUpdateForm(forms.ModelForm):
    class Meta:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        model = User
        fields = ("username", "email")
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
        return profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user  
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] #author is set automatically in views