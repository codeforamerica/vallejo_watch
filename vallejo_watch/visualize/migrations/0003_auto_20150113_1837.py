# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0002_auto_20150113_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='status',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'Pending', b'pe'), (b'OPEN', b'op'), (b'ACTIVE', b'ac'), (b'CLOSED', b'cl')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incident',
            name='x_pos',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incident',
            name='y_pos',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
