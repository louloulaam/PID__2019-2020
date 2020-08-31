from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from app.models import UserProfile


class UserSignupForm(UserCreationForm):
    """UserSignupForm custom made class"""

    class Meta:
        """Meta definition of UserSignupForm"""

        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class UserProfileSignupForm(forms.ModelForm):
    """UserProfileSignupForm custom made class"""

    class Meta:
        """Meta definition of UserProfileSignupForm"""

        model = UserProfile
        fields = ['language']


class UserUpdateForm(forms.ModelForm):
    """UserUpdateForm custom made class"""

    class Meta:
        """ Meta definitioon of UserUpdateForm"""

        model = User
        fields = [
            'last_name',
            'first_name',
            'username',
            'email',
        ]

class UserProfileUpdateForm(forms.ModelForm):
    '''UserProfileUpdateForm custom made class'''

    class Meta:
        """Meta definition of UserProfileUpdateForm"""

        model = UserProfile
        fields = ['language']
