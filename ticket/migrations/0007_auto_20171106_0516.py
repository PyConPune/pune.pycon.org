# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_userticket_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auxiliaryticket',
            name='limit',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='limit',
        ),
        migrations.AddField(
            model_name='auxiliaryticket',
            name='limits',
            field=models.PositiveIntegerField(default=0, verbose_name='limits'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='limits',
            field=models.PositiveIntegerField(default=0, verbose_name='limits'),
        ),
    ]
