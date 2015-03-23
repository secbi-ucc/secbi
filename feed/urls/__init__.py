# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'feed.views.base.inicio', name='inicio'),
                       url(r'^equipo/', 'feed.views.base.sobre', name='sobre'),
                       url(r'^proyectos/', 'feed.views.projects.proyectos', name='proyectos'),
                       url(r'^nuevoproyecto/', 'feed.views.projects.new_project', name='new_project'),
                       url(r'^agenda/', 'feed.views.base.agenda', name='agenda'),
                       )
