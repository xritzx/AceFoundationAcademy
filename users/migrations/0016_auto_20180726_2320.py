# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 17:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20180726_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='class_X_percentage',
            field=models.IntegerField(default=40, help_text='Enter the Integer Value', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(40)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact_number',
            field=models.IntegerField(blank=True, help_text='Optional Example: XXXXXXXXXX', validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(10000000000000000)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact_number_of_guardian',
            field=models.IntegerField(help_text='Required * Example: XXXXXXXXXX', validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(10000000000000000)]),
        ),
    ]
