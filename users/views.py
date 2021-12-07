from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Users
from .forms import UserForm

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


