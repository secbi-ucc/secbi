
from __future__ import unicode_literals

from django import forms
from feed.models import Project
from PIL import Image

from foro import utils
from foro.utils.markdown import Markdown


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description_short', 'description', 'cover')

    def clean_cover(self):
    	image = self.cleaned_data.get('cover',False)
    	if image:
            img = Image.open(image)
            width, height = img.size
            if height != 300 and width != 700:
    			raise forms.ValidationError("Las dimensiones de la imagen deben ser 700x300 ")
        return image

    def _get_description_html(self):
        markdown = Markdown(escape=True, hard_wrap=True)
        description_html = markdown.render(self.cleaned_data['description'])
        self.mentions = markdown.get_mentions()
        return description_html

    def save(self, commit=True):
        self.instance.description_html = self._get_description_html()
        return super(ProjectForm, self).save(commit)