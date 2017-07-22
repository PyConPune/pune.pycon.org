# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='image_base64_text',
            field=models.TextField(verbose_name='image url', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='image_base64_title',
            field=models.CharField(verbose_name='image title', null=True, blank=True, max_length=255),
        ),
    ]
