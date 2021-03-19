from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import Http404
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from PIL import Image


def home(request):
    return render(request, 'home.html')


def projects(request):

    if request.method == "GET":
        return render(request, 'add_project.html', {'myform': AddProjectForm()})

    if request.method == "POST":

        myform = AddProjectForm(request.POST)

    if request.method == "POST":
        form = AddProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'add_project.html', {'myform': myform})
