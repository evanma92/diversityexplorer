# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 12:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divexplorer', '0002_auto_20171027_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation',
            name='user',
        ),
    ]
