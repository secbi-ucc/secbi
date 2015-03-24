# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0005_auto_20150314_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='es_destacado',
            field=models.BooleanField(default=False, verbose_name='Destacado'),
            preserve_default=True,
        ),
    ]
