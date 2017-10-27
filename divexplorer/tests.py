# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.test import TestCase
from divexplorer.models import Simulation, Parameter
from django.contrib.auth.models import User
# Create your tests here.

        
class SimulationMethodTests(TestCase):
    
    def test_string_representation(self):
        simulation = Simulation(1, "2017-10-18 00:00:00", "d0", "alpha", "")
        self.assertEqual(str(simulation), str(simulation.id))
        
class ParameterMethodTests(TestCase):
    
    def test_string_representation(self):
        simulation = Simulation(1, "2017-10-18 00:00:00", "d0", "alpha", "")
        parameter = Parameter(1, simulation, 1, 1, True, False, 1, 1, 1, 1, 1, 1)
        self.assertEqual(str(parameter), str(parameter.id))
        
class ProjectTests(TestCase):
    
    def test_homepage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_aboutpage(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)