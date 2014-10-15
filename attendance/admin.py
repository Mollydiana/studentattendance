from django.contrib import admin
from attendance.models import Person, CheckIn

admin.site.register(Person)
admin.site.register(CheckIn)