#-*- coding:utf-8 -*-
from .models import Users
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = "__all__"