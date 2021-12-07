from django.db import models


# Create your models here.


class Users(models.Model):
    fname = models.CharField(verbose_name="users fname", max_length=15)
    lname = models.CharField(verbose_name="users lname", max_length=15)
    email = models.EmailField(verbose_name="users email", max_length=15)
    password = models.CharField(verbose_name="users password", max_length=1500)
    dob = models.DateField(auto_now=False, auto_now_add=False, verbose_name="user dob")
    gender = models.CharField(verbose_name="users gender", max_length=10)
    
    def __str__(self):
        return self.fname

