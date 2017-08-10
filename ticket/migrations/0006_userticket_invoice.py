# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20170727_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='userticket',
            name='invoice',
            field=models.CharField(default=0, max_length=255, verbose_name='invoice'),
        ),
    ]
