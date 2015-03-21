
from __future__ import unicode_literals

from django.db import models


class Project(models.Model):

    title = models.CharField(("title"), max_length=100)
    description_short = models.CharField(("description_short"),
                                         max_length=255, blank=True)
    description = models.CharField(("description"),
                                   max_length=1000, blank=True)
    cover = models.ImageField(upload_to='Projects', blank=True)

    otro = models.CharField(("title"), max_length=100)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
