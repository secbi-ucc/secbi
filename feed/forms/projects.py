
from __future__ import unicode_literals

from django import forms
from feed.models import Project
from PIL import Image


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description_short', 'description', 'cover')

    def clean_cover(self):
        image = self.cleaned_data.get('cover', False)
        if image:
            img = Image.open(image)
            width, height = img.size
            if height != 300 and width != 700:
                raise forms.ValidationError("Las dimensiones de la imagen deben ser 700x300 ")
        return image
