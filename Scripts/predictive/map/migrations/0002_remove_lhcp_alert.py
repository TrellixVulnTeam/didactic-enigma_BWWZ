# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lhcp',
            name='alert',
        ),
    ]
