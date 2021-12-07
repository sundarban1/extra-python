import re
from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Users
from .forms import UserForm
from operator import itemgetter

def task_create(request):
    if request.method == "POST" :
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        dob=request.POST['dob']
        gender=request.POST['gender']
        user = Users.objects.create(fname = fname, lname = lname, email = email, password= password, dob = dob,gender=gender)
        user.save()
        return redirect('/users/list/')
    else:
        return render(request, "users/users_form.html")


def listing(request):
    user_list = Users.objects.all()
    return render(request, "users/users_list.html",{"user_list":user_list})


def login(request):
    if request.method == "POST" :
        email=request.POST['email']
        password=request.POST['password']
        user_login = Users.objects.get(email=email,password = password )
        if not user_login:
            return HttpResponse(str("no user"))
        else:
            return render(request, "users/profile.html",{"user":user_login})
    else:
        return render(request, "users/login.html")
