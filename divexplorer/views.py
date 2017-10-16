# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

"""
- Each view exists as a series of individual functions.
- Each view takes in at least one argument - A HttpRequest object: convention to name it "request"
- Each view must return a HttpResponse object
"""

def index(request):
    return HttpResponse("Diversity Explorer is up and running! "
                        "<br><a href='/divexplorer/about'>About</a></br>")

def about(request):
    return HttpResponse("My CaPsT0n3 is w0nd3rfulz"
                        "<br><a href='/divexplorer/'>Back to home</a></br>")

