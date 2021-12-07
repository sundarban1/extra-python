from django.urls import path, re_path
from . import views

# namespace
app_name = 'users'

urlpatterns = [
  path('create/', views.task_create, name='task_create'),
  path('list/',views.listing,name='listing'),
  path("login/",views.login, name="login"),
]