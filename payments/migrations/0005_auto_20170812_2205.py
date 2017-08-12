# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20170812_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(max_length=255, null=True, verbose_name='currency'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=255, null=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='currency',
            field=models.CharField(max_length=255, null=True, verbose_name='currency'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='invoice_id',
            field=models.CharField(max_length=255, null=True, verbose_name='invoice_id'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.CharField(max_length=255, null=True, verbose_name='order_id'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='refund_status',
            field=models.CharField(max_length=255, null=True, verbose_name='refund_status'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(max_length=255, null=True, verbose_name='status'),
        ),
    ]
