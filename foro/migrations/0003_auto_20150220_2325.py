# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0002_auto_20140928_2347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date'], 'verbose_name': 'commentario', 'verbose_name_plural': 'comentario'},
        ),
        migrations.AlterModelOptions(
            name='commentbookmark',
            options={'verbose_name': 'marcador de comentario', 'verbose_name_plural': 'marcadores de comentarios'},
        ),
        migrations.AlterModelOptions(
            name='commentflag',
            options={'ordering': ['-date'], 'verbose_name': 'reporte de comentario', 'verbose_name_plural': 'reportes de comentarios'},
        ),
        migrations.AlterModelOptions(
            name='commenthistory',
            options={'ordering': ['-date'], 'verbose_name': 'historial de comentario', 'verbose_name_plural': 'historial de comentarios'},
        ),
        migrations.AlterModelOptions(
            name='commentlike',
            options={'ordering': ['-date'], 'verbose_name': 'me gusta', 'verbose_name_plural': 'me gusta'},
        ),
        migrations.AlterModelOptions(
            name='flag',
            options={'ordering': ['-date'], 'verbose_name': 'reporte', 'verbose_name_plural': 'reportes'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-last_active'], 'verbose_name': 'tema', 'verbose_name_plural': 'temas'},
        ),
        migrations.AlterModelOptions(
            name='topicfavorite',
            options={'ordering': ['-date'], 'verbose_name': 'favorito', 'verbose_name_plural': 'favoritos'},
        ),
        migrations.AlterModelOptions(
            name='topicnotification',
            options={'ordering': ['-date'], 'verbose_name': 'notificaci\xf3n de tema', 'verbose_name_plural': 'notificaciones de temas'},
        ),
        migrations.AlterModelOptions(
            name='topicprivate',
            options={'ordering': ['-date'], 'verbose_name': 'tema privado', 'verbose_name_plural': 'temas privados'},
        ),
        migrations.AlterModelOptions(
            name='topicunread',
            options={'ordering': ['-date'], 'verbose_name': 'tema sin leer', 'verbose_name_plural': 'temas sin leer'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined'], 'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=300, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=255, verbose_name='descripci\xf3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='cerrado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='tema privado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='is_removed',
            field=models.BooleanField(default=False, verbose_name='eliminado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(verbose_name='categoria padre', blank=True, to='foro.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=75, verbose_name='titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='action',
            field=models.IntegerField(default=0, verbose_name='acci\xf3n', choices=[(0, 'commentario'), (1, 'tema movido'), (2, 'tema cerrado'), (3, 'tema abierto'), (4, 'tema anclado'), (5, 'tema no anclado')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=3000, verbose_name='commentario'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_html',
            field=models.TextField(verbose_name='comentario html'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes_count',
            field=models.PositiveIntegerField(default=0, verbose_name='me gusta contador'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified_count',
            field=models.PositiveIntegerField(default=0, verbose_name='modificaciones contador'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(verbose_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commentbookmark',
            name='user',
            field=models.ForeignKey(verbose_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commenthistory',
            name='comment_fk',
            field=models.ForeignKey(verbose_name='comentario original', to='foro.Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commenthistory',
            name='comment_html',
            field=models.TextField(verbose_name='comentario html'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flag',
            name='body',
            field=models.TextField(verbose_name='Cuerpo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flag',
            name='reason',
            field=models.IntegerField(verbose_name='razon', choices=[(0, 'Spam'), (1, 'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(verbose_name='categoria', to='foro.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='comment_count',
            field=models.PositiveIntegerField(default=0, verbose_name='comentario contador'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='cerrado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='is_pinned',
            field=models.BooleanField(default=False, verbose_name='anclado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_active',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ultima vez activo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=75, verbose_name='titulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(verbose_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='vistos contador'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topicnotification',
            name='action',
            field=models.IntegerField(default=0, choices=[(0, 'Sin definir'), (1, 'Menci\xf3n'), (2, 'Comentario')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topicnotification',
            name='user',
            field=models.ForeignKey(verbose_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topicpoll',
            name='topic',
            field=models.OneToOneField(related_name='poll', primary_key=True, serialize=False, to='foro.Topic', verbose_name='tema'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topicunread',
            name='user',
            field=models.ForeignKey(verbose_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='comment_count',
            field=models.PositiveIntegerField(default=0, verbose_name='comentario contador'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de registro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='primer nombre', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designa si el usuario esta activo. Deselecciona estoen lugar de eliminar la cuenta.', verbose_name='activo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_administrator',
            field=models.BooleanField(default=False, verbose_name='estado administrador'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='estado moderador'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designa si el ususario puede ingresar en la administraci\xf3n', verbose_name='estado staff'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_ip',
            field=models.GenericIPAddressField(null=True, verbose_name='ultima ip', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='apellido', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(auto_now=True, verbose_name='visto por ultima vez'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=75, verbose_name='ubicaci\xf3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='timezone',
            field=models.CharField(default='UTC', max_length=32, verbose_name='zona horaria', choices=[('Etc/GMT+12', '(GMT -12:00) Eniwetok, Kwajalein'), ('Etc/GMT+11', '(GMT -11:00) Midway Island, Samoa'), ('Etc/GMT+10', '(GMT -10:00) Hawaii'), ('Pacific/Marquesas', '(GMT -9:30) Marquesas Islands'), ('Etc/GMT+9', '(GMT -9:00) Alaska'), ('Etc/GMT+8', '(GMT -8:00) Pacific Time (US & Canada)'), ('Etc/GMT+7', '(GMT -7:00) Mountain Time (US & Canada)'), ('Etc/GMT+6', '(GMT -6:00) Central Time (US & Canada), Mexico City'), ('Etc/GMT+5', '(GMT -5:00) Eastern Time (US & Canada), Bogota, Lima'), ('America/Caracas', '(GMT -4:30) Venezuela'), ('Etc/GMT+4', '(GMT -4:00) Atlantic Time (Canada), Caracas, La Paz'), ('Etc/GMT+3', '(GMT -3:00) Brazil, Buenos Aires, Georgetown'), ('Etc/GMT+2', '(GMT -2:00) Mid-Atlantic'), ('Etc/GMT+1', '(GMT -1:00) Azores, Cape Verde Islands'), ('UTC', '(GMT) Western Europe Time, London, Lisbon, Casablanca'), ('Etc/GMT-1', '(GMT +1:00) Brussels, Copenhagen, Madrid, Paris'), ('Etc/GMT-2', '(GMT +2:00) Kaliningrad, South Africa'), ('Etc/GMT-3', '(GMT +3:00) Baghdad, Riyadh, Moscow, St. Petersburg'), ('Etc/GMT-4', '(GMT +4:00) Abu Dhabi, Muscat, Baku, Tbilisi'), ('Asia/Kabul', '(GMT +4:30) Afghanistan'), ('Etc/GMT-5', '(GMT +5:00) Ekaterinburg, Islamabad, Karachi, Tashkent'), ('Asia/Kolkata', '(GMT +5:30) India, Sri Lanka'), ('Asia/Kathmandu', '(GMT +5:45) Nepal'), ('Etc/GMT-6', '(GMT +6:00) Almaty, Dhaka, Colombo'), ('Indian/Cocos', '(GMT +6:30) Cocos Islands, Myanmar'), ('Etc/GMT-7', '(GMT +7:00) Bangkok, Hanoi, Jakarta'), ('Etc/GMT-8', '(GMT +8:00) Beijing, Perth, Singapore, Hong Kong'), ('Australia/Eucla', '(GMT +8:45) Australia (Eucla)'), ('Etc/GMT-9', '(GMT +9:00) Tokyo, Seoul, Osaka, Sapporo, Yakutsk'), ('Australia/North', '(GMT +9:30) Australia (Northern Territory)'), ('Etc/GMT-10', '(GMT +10:00) Eastern Australia, Guam, Vladivostok'), ('Etc/GMT-11', '(GMT +11:00) Magadan, Solomon Islands, New Caledonia'), ('Pacific/Norfolk', '(GMT +11:30) Norfolk Island'), ('Etc/GMT-12', '(GMT +12:00) Auckland, Wellington, Fiji, Kamchatka')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='topic_count',
            field=models.PositiveIntegerField(default=0, verbose_name='contador de temas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Ingresa un nombre de usuario valido.', 'invalid')], help_text='Requerido. 30 caracteres o menos. Letras, numeros y @/./+/-/_', unique=True, verbose_name='nombre de usuario', db_index=True),
            preserve_default=True,
        ),
    ]
