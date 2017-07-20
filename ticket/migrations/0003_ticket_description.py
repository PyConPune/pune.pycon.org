# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20170717_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='description'),
        ),
    ]
