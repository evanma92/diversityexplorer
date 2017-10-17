# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-17 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divexplorer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameters',
            name='sim_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Simulation', to='divexplorer.Simulation'),
        ),
    ]