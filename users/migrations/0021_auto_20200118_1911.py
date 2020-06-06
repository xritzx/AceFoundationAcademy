# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-18 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_userprofile_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='class_X_year_of_passing',
            field=models.CharField(choices=[('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024')], max_length=5),
        ),
    ]