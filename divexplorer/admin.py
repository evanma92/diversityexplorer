# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from divexplorer.models import MyUser, Simulation, Parameter

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Simulation)
admin.site.register(Parameter)