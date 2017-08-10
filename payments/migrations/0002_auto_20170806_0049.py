# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='expire_by',
            field=models.CharField(max_length=255, null=True, verbose_name='expire_by'),
        ),
    ]
