# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20170727_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertshirt',
            options={'ordering': ['-timestamp'], 'verbose_name': 'user tshirt', 'verbose_name_plural': 'user tshirts'},
        ),
        migrations.AddField(
            model_name='usertshirt',
            name='invoice',
            field=models.CharField(default=0, max_length=255, verbose_name='invoice'),
        ),
    ]
