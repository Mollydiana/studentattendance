# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20141015_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
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
        migrations.RenameField(
            model_name='checkin',
            old_name='date',
            new_name='check_in_time',
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='person',
        ),
        migrations.AddField(
            model_name='checkin',
            name='class_name',
            field=models.ForeignKey(related_name=b'check_ins', default=2, to='attendance.Class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkin',
            name='student',
            field=models.ForeignKey(related_name=b'check_ins', default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
