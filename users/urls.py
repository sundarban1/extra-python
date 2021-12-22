from django.urls import path, re_path
from . import views

# namespace
app_name = 'users'

urlpatterns = [
  path('create/', views.task_create, name='task_create'),
  path('list/',views.listing,name='listing'),
  path("login/",views.login, name="login"),
  path("logout/",views.logout, name="logout"),
  path("passwordupdate/",views.passwordupdate, name="passwordupdate"),
  re_path(r'^(?P<pk>\d+)/delete/$', views.delete, name='delete'),
  re_path(r'^(?P<pk>\d+)/update/$', views.update, name='update'),
  re_path(r'^(?P<pk>\d+)/details/$', views.details, name='details'),
  path("forgot/",views.forgot, name="forgot"),
]