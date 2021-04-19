from django import forms
# from models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=254)
    last_name = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    passport = forms.CharField(max_length=254)
    countryid = forms.CharField(max_length=254)
    dob = forms.DateField()
    # approved = forms.BooleanField(disabled=True,)

    class Meta:
        model = User
        fields = ('username',
                    'first_name',
                    'last_name',
                    'email',
                    'dob',
                    'passport',
                    'countryid',)
                    # 'approved',
                    # 'password',)
                    # 'password1',)
