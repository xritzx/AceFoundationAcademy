# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-09-02 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20180706_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Type',
            field=models.CharField(choices=[('cogs', 'Gear Icon'), ('stethoscope', 'Medic Icon'), ('graduation-cap', 'Foundation Course')], default='cogs', max_length=15),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='subject',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Mathematics', 'Mathematics'), ('Biology', 'Biology'), ('Computer Sc.', 'Computer Sc.'), ('History/Geography', 'History/Geography'), ('Second Language', 'Second Language'), ('Others', 'Others')], default='Mathematics', max_length=20),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='dept',
            field=models.CharField(choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Mathematics', 'Mathematics'), ('Biology', 'Biology'), ('Computer Sc.', 'Computer Sc.'), ('History/Geography', 'History/Geography'), ('Second Language', 'Second Language'), ('Others', 'Others')], default='Mathematics', max_length=20),
        ),
    ]