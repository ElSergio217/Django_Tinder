# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170521_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='settings.MEDIA_ROOT/photos/avatar-1577909_640.png', upload_to='photos'),
        ),
    ]