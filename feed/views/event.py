# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from feed.forms.event import EventForm
from foro.utils.decorators import administrator_required
from django.shortcuts import get_object_or_404
from feed.models import Event
from foro.models.user import User


@administrator_required
def new_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    else:
        form = EventForm()
    return render(request, 'new_event.html', {'form': form})


def event_detail(request, id_event):
    miembros_email = User.objects.filter(es_destacado=True)
    miembros_count = User.objects.all().count()
    event = get_object_or_404(Event, pk=id_event)
    return render(request, 'event_detail.html',
                  {'event': event, 'miembros_email': miembros_email,
                   'miembros_count': miembros_count})
