# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='description',
            field=models.CharField(max_length=255, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='disabled',
            field=models.BooleanField(default=False, db_index=True, verbose_name='disabled?'),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='image_base64_text',
            field=models.TextField(null=True, verbose_name='image url', blank=True),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='image_base64_title',
            field=models.CharField(max_length=255, null=True, verbose_name='image title', blank=True),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='is_limit_reached',
            field=models.BooleanField(default=False, db_index=True, verbose_name='limit reached?'),
        ),
    ]
