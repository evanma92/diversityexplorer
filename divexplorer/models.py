# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=128, primary_key=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128, null=False)

    def __str__(self):
        """
        Purpose: to debug / access the user
        :return: The e-mail of the user
        """
        return self.email

class Simulation(models.Model):
    email = models.ForeignKey(User)
    sim_id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()

    # Each simulation has only one graph
    # Graphing parameters
    hill_num = models.CharField(max_length = 3, null=False)
    div_type = models.CharField(max_length=10, null=False)
    s3_url = models.CharField(max_length=256)


class Parameters(models.Model):
    # Each simulation can have many sets of simulation parameters
    param_id = models.IntegerField(primary_key=True)

    lsp = models.IntegerField()
    plots = models.IntegerField()
    pioneer = models.BooleanField()
    neutral = models.BooleanField()

    # for pioneers
    p_max = models.IntegerField()
    p_num = models.IntegerField()
    p_start = models.IntegerField()

    # for non-pioneers
    np_max = models.IntegerField()
    np_num = models.IntegerField()
    np_start = models.IntegerField()

class Contains(models.Model):
    param_id = models.ForeignKey(Parameters)
    sim_id = models.ForeignKey(Simulation)

