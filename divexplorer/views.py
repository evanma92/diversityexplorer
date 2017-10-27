# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from divexplorer.forms import SignUpForm

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

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/divexplorer/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


