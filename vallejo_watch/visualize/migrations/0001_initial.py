# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('address', models.CharField(max_length=256)),
                ('x_pos', models.FloatField()),
                ('y_pos', models.FloatField()),
                ('status', models.CharField(max_length=2, choices=[(b'Pending', b'pe'), (b'OPEN', b'op'), (b'ACTIVE', b'ac'), (b'CLOSED', b'cl')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IncidentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IncidentTypeMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('incident', models.ForeignKey(to='visualize.Incident')),
                ('incident_type', models.ForeignKey(to='visualize.IncidentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
