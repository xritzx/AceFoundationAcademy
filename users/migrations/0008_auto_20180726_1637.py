# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userprofile_subjects_opted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='class_XII_year_of_passing_or_expected',
            field=models.IntegerField(help_text='Optional, Only in case of dropper'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='class_X_year_of_passing',
            field=models.IntegerField(),
        ),
    ]
