# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-09-02 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20190902_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='class_XII_board_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='class_XII_marksheet',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='class_XII_percentage',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='class_XII_year_of_passing_or_expected',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='class_X_marksheet',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='class_X_percentage',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='fresher_or_dropper',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='subjects_opted',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_exam_marksheet',
            field=models.ImageField(blank=True, help_text="Marksheet should name as 'YOUR_NAME_CLASS' ", upload_to='users/marksheet'),
        ),
    ]
