# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-04 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161004_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
