# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from . import register
from foro.forms.search import BasicSearchForm


@register.inclusion_tag('foro/search/_form.html')
def render_search_form():
    form = BasicSearchForm()
    return {'form': form, }


@register.assignment_tag()
def get_topics_from_search_result(results):
    # Since Im only indexing Topics this is ok.
    topics = [r.object for r in results]
    return topics
