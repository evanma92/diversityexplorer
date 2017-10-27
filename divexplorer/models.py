# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.

class Simulation(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', null=False)
    id = models.PositiveIntegerField(primary_key=True)
    date = models.DateTimeField()

    # Each simulation has only one graph
    # Graphing parameters
    hill_num = models.CharField(max_length=3)
    div_type = models.CharField(max_length=10)
    s3_url = models.CharField(max_length=256)
    
    def __str__(self):
        return str(self.id)


class Parameter(models.Model):
    # Each simulation can have many sets of simulation parameters
    simulation = models.ForeignKey('Simulation', to_field='id', on_delete=models.CASCADE)
    id = models.PositiveIntegerField(primary_key=True)

    lsp = models.PositiveIntegerField()
    plots = models.PositiveIntegerField()
    pioneer = models.BooleanField()
    neutral = models.BooleanField()

    # for pioneers
    p_max = models.PositiveIntegerField()
    p_num = models.PositiveIntegerField()
    p_start = models.PositiveIntegerField()

    # for non-pioneers
    np_max = models.PositiveIntegerField()
    np_num = models.PositiveIntegerField()
    np_start = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)
