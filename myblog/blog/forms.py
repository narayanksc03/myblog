
# from tkinter import Widget
from django.forms import PasswordInput
# from django.db import models
from django import forms
from blog.models import AppUser

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AppUser
        #fields = "__all__"
        fields = ('first_name','middle_name','last_name','email','contact')
#__all__ -> generates form of all fields in the model
#selective field-> we need to define tuple
