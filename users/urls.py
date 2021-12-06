from django.urls import path, re_path
from . import views

# namespace
app_name = 'users'

urlpatterns = [
    # Create a task
    path('signup/', views.TaskCreateUser.as_view(), name='signup'),
]