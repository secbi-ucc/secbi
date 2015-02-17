# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

import djconfig

from foro.forms.admin import BasicConfigForm

# TODO: use app loader in django 1.7
djconfig.register(BasicConfigForm)

urlpatterns = patterns('',
                       url(r'^$', 'foro.views.topic.topics_active', name='index'),
                       url(r'^st/admin/', include('foro.urls.admin')),
                       url(r'^category/', include('foro.urls.category')),
                       url(r'^topic/', include('foro.urls.topic')),
                       url(r'^topic/unread/', include('foro.urls.topic_unread')),
                       url(r'^topic/notification/', include('foro.urls.topic_notification')),
                       url(r'^topic/favorite/', include('foro.urls.topic_favorite')),
                       url(r'^topic/private/', include('foro.urls.topic_private')),
                       url(r'^topic/poll/', include('foro.urls.topic_poll')),
                       url(r'^comment/', include('foro.urls.comment')),
                       url(r'^comment/bookmark/', include('foro.urls.comment_bookmark')),
                       url(r'^comment/flag/', include('foro.urls.comment_flag')),
                       url(r'^comment/history/', include('foro.urls.comment_history')),
                       url(r'^comment/like/', include('foro.urls.comment_like')),
                       url(r'^user/', include('foro.urls.user')),
                       url(r'^search/', include('foro.urls.search')),
                       )
