# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0003_auto_20150113_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidenttypemap',
            name='incident',
        ),
        migrations.RemoveField(
            model_name='incidenttypemap',
            name='incident_type',
        ),
        migrations.DeleteModel(
            name='IncidentType',
        ),
        migrations.DeleteModel(
            name='IncidentTypeMap',
        ),
        migrations.AddField(
            model_name='incident',
            name='description',
            field=models.CharField(max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='incident',
            name='issue_type',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'Noise Complaint', b'nc'), (b'Graffiti', b'gr')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incident',
            name='status',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'Pending', b'pe'), (b'Assigned', b'as'), (b'Inactive', b'in'), (b'Closed as Resolved', b'cl')]),
            preserve_default=True,
        ),
    ]
