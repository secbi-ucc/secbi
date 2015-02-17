# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$', 'foro.views.admin.index.dashboard', name='admin'),
                       url(r'^index/', include('foro.urls.admin.index')),
                       url(r'^category/', include('foro.urls.admin.category')),
                       url(r'^comment/flag/', include('foro.urls.admin.comment_flag')),
                       url(r'^config/', include('foro.urls.admin.config')),
                       url(r'^topic/', include('foro.urls.admin.topic')),
                       url(r'^user/', include('foro.urls.admin.user')),
                       )
