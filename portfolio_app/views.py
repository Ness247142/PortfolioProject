from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import Http404
from .forms import *
from django.views.generic import *
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from PIL import Image


class HomeView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'projects'
    ordering = ['id']


class ProjectIndexView(ListView):
    model = Project
    template_name = 'project_index.html'
    context_object_name = 'projects'
    ordering = ['id']


def add_projects(request):

    if request.method == "GET":
        return render(request, 'add_project.html', {'myform': AddProjectForm()})

    if request.method == "POST":

        myform = AddProjectForm(request.POST)

    if request.method == "POST":
        form = AddProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('project_index')
        else:
            return render(request, 'add_project.html', {'myform': myform})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # Update Posts
    model = Project
    template_name = 'update_project.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.kwargs['pk']})


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project_index')

    def test_func(self):
        category = self.get_object()
        if self.request.user:
            return True
        return False
