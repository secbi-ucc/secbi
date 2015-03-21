# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description_short', models.CharField(max_length=255, verbose_name='description_short', blank=True)),
                ('description', models.CharField(max_length=1000, verbose_name='description', blank=True)),
                ('cover', models.ImageField(upload_to='Projects', blank=True)),
                ('otro', models.CharField(max_length=100, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model,),
        ),
    ]
