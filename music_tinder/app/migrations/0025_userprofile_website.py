# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20170521_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=''),
        ),
    ]