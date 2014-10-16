# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20141016_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('class_start', models.DateTimeField()),
                ('class_end', models.DateTimeField()),
                ('student', models.ManyToManyField(related_name=b'class_student', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(related_name=b'class_teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='class',
            name='student',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='checkin',
            name='class_name',
            field=models.ForeignKey(related_name=b'check_ins', to='attendance.Course'),
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
