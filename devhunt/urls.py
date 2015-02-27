# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Reemplazar el login para el admin por seguridad
from django.contrib.auth.decorators import login_required
admin.site.login = login_required(admin.site.login)

urlpatterns = patterns('',
                       url(r'^$', include('feed.urls',
                                          namespace="feed",
                                          app_name="feed")),
                       url(r'^discusion/', include('foro.urls',
                                                   namespace="foro",
                                                   app_name="foro")),
                       )
# Servir archivos estaticos para desarrollo local

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
