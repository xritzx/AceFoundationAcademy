# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_gallery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Type',
            field=models.CharField(choices=[('cogs', 'Engineering'), ('stethoscope', 'Medical'), ('graduation-cap', 'Foundation Course')], default='cogs', max_length=15),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='subject',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Mathematics', 'Mathematics'), ('Biology', 'Biology'), ('Computer', 'Computer'), ('Others', 'Others')], default='Mathematics', max_length=20),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dept',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Mathematics', 'Mathematics'), ('Biology', 'Biology'), ('Computer', 'Computer'), ('Others', 'Others')], default='Mathematics', max_length=20),
        ),
    ]