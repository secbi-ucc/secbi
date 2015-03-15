# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0004_auto_20150220_2352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date'], 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='commentbookmark',
            options={'verbose_name': 'comment bookmark', 'verbose_name_plural': 'comments bookmarks'},
        ),
        migrations.AlterModelOptions(
            name='commentflag',
            options={'ordering': ['-date'], 'verbose_name': 'comment flag', 'verbose_name_plural': 'comments flags'},
        ),
        migrations.AlterModelOptions(
            name='commenthistory',
            options={'ordering': ['-date'], 'verbose_name': 'comment history', 'verbose_name_plural': 'comments history'},
        ),
        migrations.AlterModelOptions(
            name='commentlike',
            options={'ordering': ['-date'], 'verbose_name': 'like', 'verbose_name_plural': 'likes'},
        ),
        migrations.AlterModelOptions(
            name='flag',
            options={'ordering': ['-date'], 'verbose_name': 'flag', 'verbose_name_plural': 'flags'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-last_active'], 'verbose_name': 'topic', 'verbose_name_plural': 'topics'},
        ),
        migrations.AlterModelOptions(
            name='topicfavorite',
            options={'ordering': ['-date'], 'verbose_name': 'favorite', 'verbose_name_plural': 'favorites'},
        ),
        migrations.AlterModelOptions(
            name='topicnotification',
            options={'ordering': ['-date'], 'verbose_name': 'topic notification', 'verbose_name_plural': 'topics notification'},
        ),
        migrations.AlterModelOptions(
            name='topicprivate',
            options={'ordering': ['-date'], 'verbose_name': 'private topic', 'verbose_name_plural': 'private topics'},
        ),
        migrations.AlterModelOptions(
            name='topicunread',
            options={'ordering': ['-date'], 'verbose_name': 'topic unread', 'verbose_name_plural': 'topics unread'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=255, verbose_name='description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='closed'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='private'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='is_removed',
            field=models.BooleanField(default=False, verbose_name='removed'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(verbose_name='category parent', blank=True, to='foro.Category', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=75, verbose_name='title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='action',
            field=models.IntegerField(default=0, verbose_name='action', choices=[(0, 'comment'), (1, 'topic moved'), (2, 'topic closed'), (3, 'topic unclosed'), (4, 'topic pinned'), (5, 'topic unpinned')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=3000, verbose_name='comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_html',
            field=models.TextField(verbose_name='comment html'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes_count',
            field=models.PositiveIntegerField(default=0, verbose_name='likes count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='modified_count',
            field=models.PositiveIntegerField(default=0, verbose_name='modified count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commentbookmark',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commenthistory',
            name='comment_fk',
            field=models.ForeignKey(verbose_name='original comment', to='foro.Comment'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commenthistory',
            name='comment_html',
            field=models.TextField(verbose_name='comment html'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flag',
            name='body',
            field=models.TextField(verbose_name='body', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flag',
            name='reason',
            field=models.IntegerField(verbose_name='reason', choices=[(0, 'Spam'), (1, 'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='foro.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='comment_count',
            field=models.PositiveIntegerField(default=0, verbose_name='comment count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='closed'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='is_pinned',
            field=models.BooleanField(default=False, verbose_name='pinned'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_active',
            field=models.DateTimeField(auto_now_add=True, verbose_name='last active'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=75, verbose_name='title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='view_count',
            field=models.PositiveIntegerField(default=0, verbose_name='views count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topicnotification',
            name='action',
            field=models.IntegerField(default=0, choices=[(0, 'Undefined'), (1, 'Mention'), (2, 'Comment')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topicnotification',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topicpoll',
            name='topic',
            field=models.OneToOneField(related_name='poll', primary_key=True, serialize=False, to='foro.Topic', verbose_name='topic'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topicunread',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='comment_count',
            field=models.PositiveIntegerField(default=0, verbose_name='comment count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.CharField(max_length=80, null=True, verbose_name='Universidad/Empresa', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='github_username',
            field=models.CharField(max_length=30, null=True, verbose_name='Usuario en github', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_administrator',
            field=models.BooleanField(default=False, verbose_name='administrator status'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='moderator status'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_ip',
            field=models.GenericIPAddressField(null=True, verbose_name='last ip', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_seen',
            field=models.DateTimeField(auto_now=True, verbose_name='last seen'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='linkedin_url',
            field=models.URLField(null=True, verbose_name='Url perfil likedin', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=75, verbose_name='location', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='timezone',
            field=models.CharField(default='Etc/GMT+5', max_length=32, verbose_name='time zone', choices=[('Etc/GMT+12', '(GMT -12:00) Eniwetok, Kwajalein'), ('Etc/GMT+11', '(GMT -11:00) Midway Island, Samoa'), ('Etc/GMT+10', '(GMT -10:00) Hawaii'), ('Pacific/Marquesas', '(GMT -9:30) Marquesas Islands'), ('Etc/GMT+9', '(GMT -9:00) Alaska'), ('Etc/GMT+8', '(GMT -8:00) Pacific Time (US & Canada)'), ('Etc/GMT+7', '(GMT -7:00) Mountain Time (US & Canada)'), ('Etc/GMT+6', '(GMT -6:00) Central Time (US & Canada), Mexico City'), ('Etc/GMT+5', '(GMT -5:00) Eastern Time (US & Canada), Bogota, Lima'), ('America/Caracas', '(GMT -4:30) Venezuela'), ('Etc/GMT+4', '(GMT -4:00) Atlantic Time (Canada), Caracas, La Paz'), ('Etc/GMT+3', '(GMT -3:00) Brazil, Buenos Aires, Georgetown'), ('Etc/GMT+2', '(GMT -2:00) Mid-Atlantic'), ('Etc/GMT+1', '(GMT -1:00) Azores, Cape Verde Islands'), ('UTC', '(GMT) Western Europe Time, London, Lisbon, Casablanca'), ('Etc/GMT-1', '(GMT +1:00) Brussels, Copenhagen, Madrid, Paris'), ('Etc/GMT-2', '(GMT +2:00) Kaliningrad, South Africa'), ('Etc/GMT-3', '(GMT +3:00) Baghdad, Riyadh, Moscow, St. Petersburg'), ('Etc/GMT-4', '(GMT +4:00) Abu Dhabi, Muscat, Baku, Tbilisi'), ('Asia/Kabul', '(GMT +4:30) Afghanistan'), ('Etc/GMT-5', '(GMT +5:00) Ekaterinburg, Islamabad, Karachi, Tashkent'), ('Asia/Kolkata', '(GMT +5:30) India, Sri Lanka'), ('Asia/Kathmandu', '(GMT +5:45) Nepal'), ('Etc/GMT-6', '(GMT +6:00) Almaty, Dhaka, Colombo'), ('Indian/Cocos', '(GMT +6:30) Cocos Islands, Myanmar'), ('Etc/GMT-7', '(GMT +7:00) Bangkok, Hanoi, Jakarta'), ('Etc/GMT-8', '(GMT +8:00) Beijing, Perth, Singapore, Hong Kong'), ('Australia/Eucla', '(GMT +8:45) Australia (Eucla)'), ('Etc/GMT-9', '(GMT +9:00) Tokyo, Seoul, Osaka, Sapporo, Yakutsk'), ('Australia/North', '(GMT +9:30) Australia (Northern Territory)'), ('Etc/GMT-10', '(GMT +10:00) Eastern Australia, Guam, Vladivostok'), ('Etc/GMT-11', '(GMT +11:00) Magadan, Solomon Islands, New Caledonia'), ('Pacific/Norfolk', '(GMT +11:30) Norfolk Island'), ('Etc/GMT-12', '(GMT +12:00) Auckland, Wellington, Fiji, Kamchatka')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='topic_count',
            field=models.PositiveIntegerField(default=0, verbose_name='topic count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='trello_username',
            field=models.CharField(max_length=30, null=True, verbose_name='Usuario en Trello', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], help_text='Requerido. 30 caracteres o menos. Letras, Numeros y caracteres especiales@/./+/-/_ solamente', unique=True, verbose_name='Nombre de usuario', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='web_site',
            field=models.URLField(null=True, verbose_name='Sitio web', blank=True),
            preserve_default=True,
        ),
    ]
