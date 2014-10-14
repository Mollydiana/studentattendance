from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Person(AbstractUser):
    teacher = models.BooleanField(default=False)


class CheckIn(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Person, related_name='attendancecount')