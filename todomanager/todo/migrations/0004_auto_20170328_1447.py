# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20170328_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('group', models.ForeignKey(related_name='todo_relation_group', null=True, to='todo.Group', blank=True, verbose_name='Group')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, default=datetime.datetime(2017, 3, 29, 14, 47, 54, 346732, tzinfo=utc), verbose_name='Fin prévue le'),
        ),
    ]
