from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(verbose_name="User name", max_length=65, unique=True)
    gender = models.CharField(verbose_name="User gender", max_length=65)

    def __str__(self):
        return self.name