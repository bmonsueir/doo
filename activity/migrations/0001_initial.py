# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=255)),
                ('weight1', models.IntegerField(default=0)),
                ('weight2', models.IntegerField(default=0)),
                ('weight3', models.IntegerField(default=0)),
                ('weight4', models.IntegerField(default=0)),
            ],
        ),
    ]
