# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20170806_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tshirt',
            name='limit',
        ),
        migrations.AddField(
            model_name='tshirt',
            name='limits',
            field=models.PositiveIntegerField(default=0, verbose_name='limits'),
        ),
    ]
