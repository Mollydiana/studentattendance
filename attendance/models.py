from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Person(AbstractUser):
    teacher = models.BooleanField(default=True)




class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Person, related_name="class_teacher")
    student = models.ManyToManyField(Person, related_name="class_student")
    class_start = models.DateTimeField()
    class_end = models.DateTimeField()


class CheckIn(models.Model):
    student = models.ForeignKey(Person, related_name='check_ins')
    class_name = models.ForeignKey(Course, related_name="check_ins")
    check_in_time = models.DateTimeField(auto_now_add=True)