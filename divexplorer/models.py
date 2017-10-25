# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class MyUser(AbstractBaseUser):
    email = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True   )
    USERNAME_FIELD = 'email'


class Simulation(models.Model):
    email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sim_id = models.PositiveIntegerField(primary_key=True)
    date = models.DateTimeField()

    # Each simulation has only one graph
    # Graphing parameters
    hill_num = models.CharField(max_length = 3, null=False)
    div_type = models.CharField(max_length=10, null=False)
    s3_url = models.CharField(max_length=256)
    
    def __str__(self):
        return str(self.sim_id)


class Parameter(models.Model):
    # Each simulation can have many sets of simulation parameters
    param_id = models.PositiveIntegerField(primary_key=True)
    sim_id = models.ForeignKey(Simulation, related_name="Simulation", null=True, on_delete=models.CASCADE)

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
        return str(self.param_id)
