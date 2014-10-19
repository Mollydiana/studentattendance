from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    teacher = models.BooleanField(default=False)
    count = models.IntegerField(default=0)


class CheckIn(models.Model):
    student = models.ForeignKey(Profile)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{}'.format(self.student, self.time)