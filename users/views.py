from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Users
from .forms import UserForm

def task_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done!!")
    else:
        form = UserForm()

    return render(request, "users/users_form.html", { "form": form, })



