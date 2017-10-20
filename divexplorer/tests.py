# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.test import TestCase
from divexplorer.models import User
# Create your tests here.

class UserMethodTests(TestCase):
    
    def test_string_representation(self):
        user = User(email="evanma92@gmail.com", username = "evanma92", password = "123456")
        self.assertEqual(str(user), user.email)
        
class ProjectTests(TestCase):
    
    def test_homepage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_aboutpage(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)