# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from . import register
from foro.models.topic_favorite import TopicFavorite
from foro.forms.topic_favorite import FavoriteForm


@register.inclusion_tag('foro/topic_favorite/_form.html')
def render_favorite_form(topic, user, next=None):
    try:
        favorite = TopicFavorite.objects.get(user=user, topic=topic)
    except TopicFavorite.DoesNotExist:
        favorite = None

    form = FavoriteForm()
    return {'form': form, 'topic_id': topic.pk, 'favorite': favorite, 'next': next}
