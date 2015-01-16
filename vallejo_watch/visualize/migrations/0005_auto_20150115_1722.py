# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0004_auto_20150114_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='status',
        ),
        migrations.AlterField(
            model_name='incident',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='incident',
            name='issue_type',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'nc', b'Noise Complaint'), (b'gr', b'Graffiti'), (b'dr', b'Drug Activity'), (b'vn', b'Vandalism'), (b've', b'Vehicle'), (b'bl', b'Burglary'), (b'an', b'Animal')]),
            preserve_default=True,
        ),
    ]
