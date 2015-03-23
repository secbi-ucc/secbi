# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='otro',
        ),
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ImageField(upload_to='Projects_cover', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Descripci\xf3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description_short',
            field=models.CharField(max_length=255, verbose_name='Descripci\xf3n Corta', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
            preserve_default=True,
        ),
    ]
