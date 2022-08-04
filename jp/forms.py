from django import forms
from django.contrib.auth.models import User

from jp.models import Blog


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username','password'}


class AddBlogForms(forms.ModelForm):


    class Meta:
        model=Blog
        fields='__all__'