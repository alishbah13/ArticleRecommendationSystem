from django import forms
from models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',
                    'first_name',
                    'last_name',
                    'email',
                    'dob',
                    'password',
                    'passport',
                    'countryid',
                    'approved')