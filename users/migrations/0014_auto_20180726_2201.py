# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 16:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180726_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='class_XII_board_name',
            field=models.CharField(blank=True, choices=[('CBSE', 'CBSE'), ('ICSE', 'ICSE'), ('WBSE', 'WBSE')], default='None', help_text='Optional, Only in case of dropper', max_length=6),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='class_XII_percentage',
            field=models.IntegerField(blank=True, default=0, help_text='Optional, Only in case of dropper', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='class_XII_year_of_passing_or_expected',
            field=models.CharField(blank=True, choices=[(2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], help_text='Optional, Only in case of dropper', max_length=5),
        ),
    ]