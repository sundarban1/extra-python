from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Users
from .forms import UserForm
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

class TaskCreateUser(CreateView):
    model = Users
    form_class = UserForm
    success_url = reverse_lazy('users:users_form')



