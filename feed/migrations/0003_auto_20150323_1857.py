# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20150322_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_html',
            field=models.TextField(default='America/Bogota', verbose_name='Descripci\xf3n HTML'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ImageField(upload_to='Projects_cover'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=4000, verbose_name='Descripci\xf3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description_short',
            field=models.CharField(max_length=255, verbose_name='Descripci\xf3n Corta'),
            preserve_default=True,
        ),
    ]
