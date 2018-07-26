# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-26 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180726_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='gardian_contact_number',
            new_name='contact_number_of_guardian',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='gardian_name',
            new_name='guardian_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fresher_or_dropper',
            field=models.CharField(choices=[('Fresher', 'Fresher'), ('Dropper', 'Dropper')], default='Fresher', help_text='Enter wheather a Fresher or not', max_length=10),
        ),
    ]
