# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20170328_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='member',
            field=models.ForeignKey(verbose_name='Member', related_name='todo_relation_member', blank=True, null=True, to='todo.Member'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(null=True, default=datetime.datetime(2017, 3, 29, 14, 58, 2, 569605, tzinfo=utc), verbose_name='Fin prévue le', blank=True),
        ),
    ]
