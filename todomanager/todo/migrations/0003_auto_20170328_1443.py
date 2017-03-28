# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170328_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(verbose_name='Crée le', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='Modifié le', auto_now=True)),
                ('avatar', models.ImageField(blank=True, upload_to='', null=True)),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='settings',
            field=models.ForeignKey(to='todo.Setting', related_name='todo_member_setting', verbose_name='Paramètres', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fin prévue le', default=datetime.datetime(2017, 3, 29, 14, 43, 26, 802877, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(to='todo.Member', related_name='todo_group_creator', verbose_name='Créé par', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='modified_by',
            field=models.ForeignKey(to='todo.Member', related_name='todo_group_modificator', verbose_name='Modifié par', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='settings',
            field=models.ForeignKey(to='todo.Setting', related_name='todo_group_setting', verbose_name='Paramètres', blank=True, null=True),
        ),
    ]
