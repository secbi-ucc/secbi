
from __future__ import unicode_literals

from django import forms
from feed.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'description_short', 'post_text', 'due_date',
                  'lugar', 'tipo')
