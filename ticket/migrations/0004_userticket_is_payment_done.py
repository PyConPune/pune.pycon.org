# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20170722_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='userticket',
            name='is_payment_done',
            field=models.BooleanField(default=False, verbose_name='payment done?'),
        ),
    ]
