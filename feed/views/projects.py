# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from feed.forms.projects import ProjectForm
from foro.utils.decorators import administrator_required
from feed.models import Project


def proyectos(request):
    proyectos = Project.objects.all()
    return render(request, 'projects/proyectos.html', {"proyectos": proyectos})


def ver_project(request, pk):
    proyecto = get_object_or_404(Project, id=pk)
    return render(request, 'projects/ver_project.html', {"proyecto": proyecto})


@administrator_required
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('feed:proyectos'))
    else:
        form = ProjectForm()

    return render(request, 'projects/new_project.html', {'form': form})


@administrator_required
def edit_project(request, pk):
    proyecto = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=proyecto)
        if form.is_valid():
            form.save()
    else:
        form = ProjectForm(instance=proyecto)

    return render(request, 'projects/edit_project.html', {'form': form})
