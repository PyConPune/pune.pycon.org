# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_order_payment_razorpaykeys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razorpaykeys',
            name='api_key',
            field=models.CharField(max_length=255, verbose_name='api key'),
        ),
        migrations.AlterField(
            model_name='razorpaykeys',
            name='api_secret',
            field=models.CharField(max_length=255, verbose_name='api secret'),
        ),
    ]
