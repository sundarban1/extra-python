from django.urls import path, re_path
from . import views

# namespace
app_name = 'users'

urlpatterns = [
    # Create a task
      path('create/', views.task_create, name='task_create')
]