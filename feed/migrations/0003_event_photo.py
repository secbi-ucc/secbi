# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20150322_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description_short', models.CharField(max_length=255, verbose_name='Descripci\xf3n corta')),
                ('post_text', models.TextField(verbose_name='Descripci\xf3n larga')),
                ('due_date', models.DateTimeField(verbose_name='Fecha y hora')),
                ('lugar', models.CharField(max_length=100, verbose_name='Lugar')),
                ('tipo', models.CharField(default='EV', max_length=2, choices=[('EV', 'Evento'), ('RE', 'Reuni\xf3n')])),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('summary', models.TextField(null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='photos/%Y/%m')),
                ('evento', models.ForeignKey(to='feed.Event')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
            bases=(models.Model,),
        ),
    ]
