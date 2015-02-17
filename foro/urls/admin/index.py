# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns("foro.views.admin.index",
                       url(r'^$', 'dashboard', name='admin-dashboard'),
                       )
