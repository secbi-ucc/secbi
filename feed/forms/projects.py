# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from feed.models.projects import Project
	
class ProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields =('title','description_short','description','cover')
