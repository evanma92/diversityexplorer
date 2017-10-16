# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

"""
- Each view exists as a series of individual functions.
- Each view takes in at least one argument - A HttpRequest object: convention to name it "request"
- Each view must return a HttpResponse object
"""

def index(request):
    context_dict = {'boldmessage': "Working with Maurice and Michiel on the best capstone ever"}

    return render(request, 'divexplorer/index.html', context=context_dict)

def about(request):
    return HttpResponse("My CaPsT0n3 is w0nd3rfulz"
                        "<br><a href='/divexplorer/'>Back to home</a></br>")

