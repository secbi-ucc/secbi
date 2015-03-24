# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Project(models.Model):

    title = models.CharField(("Titulo"), max_length=100)
    description_short = models.CharField(("Descripción Corta"), max_length=255)
    description = models.TextField(("Descripción"), max_length=4000)
    description_html = models.TextField(("Descripción HTML"))
    cover = models.ImageField(upload_to='Projects_cover')

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Event(models.Model):
    EVENTO = 'EV'
    REUNION = 'RE'
    EVENT_TYPE_CHOICES = (
        (EVENTO, 'Evento'),
        (REUNION, 'Reunión')
    )
    title = models.CharField(("Titulo"), max_length=100)
    description_short = models.CharField(("Descripción corta"),
                                         max_length=255, blank=False)
    post_text = models.TextField(("Descripción larga"))
    due_date = models.DateTimeField(("Fecha y hora"))
    lugar = models.CharField(("Lugar"), max_length=100)
    tipo = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES,
                            default=EVENTO)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


class Photo(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos/%Y/%m')
    evento = models.ForeignKey(Event)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
