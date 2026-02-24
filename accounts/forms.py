from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))

    class Meta:
        model = User
        fields = ['email']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # No editable profile fields (we removed bio/location/website/avatar)
        fields = []
