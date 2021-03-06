# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-09-02 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20190902_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_exam_marksheet',
            field=models.ImageField(blank=True, help_text="Marksheet should name as 'YOUR_NAME_CLASS' less than 200kB", upload_to='users/marksheet'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, help_text='Image should be less than 200kB', upload_to='users/profile_pic'),
        ),
    ]
