# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from feed.forms.projects import ProjectForm
from foro.utils.decorators import administrator_required

@administrator_required
def new_project(request):
	if request.method == 'POST':
		form = ProjectForm(data=request.POST)

		if form.is_valid():
			project = form.save()

			return redirect(reverse('feed:proyectos'))

	else:
		form = ProjectForm()
	return render(request,'new_project.html',{'form':form})