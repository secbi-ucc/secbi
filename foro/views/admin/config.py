# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import ugettext as _

from foro.utils.decorators import administrator_required

from foro.forms.admin import BasicConfigForm


@administrator_required
def config_basic(request):

    if request.method == 'POST':
        form = BasicConfigForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, _("Settings updated!"))
            return redirect(request.GET.get("next", request.get_full_path()))
    else:
        form = BasicConfigForm()

    return render(request, 'foro/admin/config/config_basic.html', {'form': form, })
