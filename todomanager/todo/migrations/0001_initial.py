# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('avatar', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(verbose_name='Crée le', auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modifié le')),
                ('notify_mail', models.BooleanField(verbose_name='Notification par mail', default=False)),
                ('notify_sms', models.BooleanField(verbose_name='Notification par sms', default=False)),
                ('created_by', models.ForeignKey(null=True, related_name='todo_setting_creator', verbose_name='Créé par', to='todo.Member')),
                ('modified_by', models.ForeignKey(null=True, related_name='todo_setting_modificator', verbose_name='Modifié par', to='todo.Member')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_at', models.DateTimeField(verbose_name='Crée le', auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modifié le')),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description', null=True, blank=True)),
                ('due_date', models.DateTimeField(verbose_name='Fin prévue le', null=True, blank=True, default=datetime.datetime(2017, 3, 29, 13, 36, 2, 53752, tzinfo=utc))),
                ('completed', models.BooleanField(verbose_name='Tache terminée ? ', default=False)),
                ('status', models.CharField(max_length=20, choices=[(None, '---')], null=True, blank=True, default=None)),
                ('assigned_to', models.ForeignKey(null=True, blank=True, related_name='tasks_assigned', verbose_name='Assigné à', to='todo.Member')),
                ('created_by', models.ForeignKey(null=True, related_name='todo_task_creator', verbose_name='Créé par', to='todo.Member')),
                ('modified_by', models.ForeignKey(null=True, related_name='todo_task_modificator', verbose_name='Modifié par', to='todo.Member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='settings',
            field=models.ForeignKey(null=True, related_name='todo_member_setting', verbose_name='Paramètres', to='todo.Setting'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
