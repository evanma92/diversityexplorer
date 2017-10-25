# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-25 05:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('param_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('lsp', models.PositiveIntegerField()),
                ('plots', models.PositiveIntegerField()),
                ('pioneer', models.BooleanField()),
                ('neutral', models.BooleanField()),
                ('p_max', models.PositiveIntegerField()),
                ('p_num', models.PositiveIntegerField()),
                ('p_start', models.PositiveIntegerField()),
                ('np_max', models.PositiveIntegerField()),
                ('np_num', models.PositiveIntegerField()),
                ('np_start', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('sim_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('hill_num', models.CharField(max_length=3)),
                ('div_type', models.CharField(max_length=10)),
                ('s3_url', models.CharField(max_length=256)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='parameter',
            name='sim_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Simulation', to='divexplorer.Simulation'),
        ),
    ]
