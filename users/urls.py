#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'users'

urlpatterns = [
    # # Retrieve task list
     path('list/', views.user_list, name='task_list'),
    # # # Create a task
    #  path('create/', views.task_create, name='task_create'),
    # # # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.user_details, name='user_details'),
    # # # Update a task
    #  re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # # # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.user_delete, name='user_delete'),
]