# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-16 06:15
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20180516_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='image',
            field=stdimage.models.StdImageField(upload_to='..static/base/img/team'),
        ),
    ]
