from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Person(AbstractUser):
    teacher = models.BooleanField(default=True)


class CheckIn(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(Person, related_name='checkins')
