import re
from django.forms.widgets import PasswordInput
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Users
from .forms import UserForm
from operator import itemgetter
from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import message, send_mail
from django.utils.crypto import get_random_string


def task_create(request):
    if request.method == "POST" :
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        dob=request.POST['dob']
        gender=request.POST['gender']
        user = Users.objects.create(fname = fname, lname = lname, email = email, password= password, dob = dob,gender=gender)
        user.save()
        send_mail(
            'user created',
            'welcome to my user app',
            'myapp@gmail.com',
            [email,'sundar@gmail.com'],
            fail_silently= False,
        )
        return redirect('/users/list/')
    else:
        return render(request, "users/users_form.html")


def listing(request):
    if 'login' not in request.session:
        return redirect('/users/login')
    else:
        user_list = Users.objects.all()
        return render(request, "users/users_list.html",{"user_list":user_list})


def login(request):
    if request.method == "POST" :
        email=request.POST['email']
        password=request.POST['password']
        user_login = Users.objects.get(email=email)
        if not check_password(password,user_login.password):
            return HttpResponse('invalid password and email')
        if not user_login:
            return HttpResponse(str("no user"))
        else:
            request.session['login'] = 'true'
            request.session['user_id'] = user_login.id
            send_mail(
            'login sucessful',
            'you have logged in sucessfully in myapp',
            'myapp@gmail.com',
            [email],
            fail_silently= False,
        )
            return render(request, "users/profile.html",{"user":user_login})

    else:
        return render(request, "users/login.html")

def logout(request):
    del request.session['login']
    return render(request, "users/login.html")

def delete(request,pk):
    if int(pk)==int(request.session['user_id']):
        return HttpResponse("invalid")
    else:
        user_obj = get_object_or_404(Users, pk=pk)
        user_obj.delete()
        return redirect('/users/list/')

def update(request,pk):
    if request.method == "POST" :
        id=int(request.POST['userid'])
        user =  Users.objects.get(id=id)
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.email=request.POST['email']
        user.dob=request.POST['dob']
        user.gender=request.POST['gender']
        user.save()
        return redirect('/users/list/')
    else:
        user_obj = get_object_or_404(Users, pk=pk)
        return render(request, "users/update.html",{"user":user_obj})

    

def details(request,pk):
    user_obj = get_object_or_404(Users, pk=pk)
    return render(request, "users/profile.html",{"user":user_obj})

def forgot(request):
    if request.method=="POST":
        email=request.POST['email']
        password = get_random_string(length=32) #generating andom passwod
        user =  Users.objects.get(email=email)
        user.password=make_password(password) #storing random string on database
        user.save()
        #sending hashed pasword
        send_mail(
            'temprory password',
            'your pass word is '+password,
            'myapp@gmail.com',
            [email],
            fail_silently= False,
        )
        return redirect('/users/login')
    else:   
        return render(request,'users/forgot_pwd.html')
    
def passwordupdate(request):
    return render(request,'users/new_password.html')









