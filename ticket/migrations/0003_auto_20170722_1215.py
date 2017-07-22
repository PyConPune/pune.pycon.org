# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20170722_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='disabled',
            field=models.BooleanField(db_index=True, default=False, verbose_name='disabled?'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_limit_reached',
            field=models.BooleanField(db_index=True, default=False, verbose_name='limit reached?'),
        ),
    ]
