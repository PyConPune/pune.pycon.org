# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('invoice_id', models.CharField(max_length=255, verbose_name='invoice_id')),
                ('receipt_number', models.CharField(max_length=255, verbose_name='receipt_number')),
                ('order_id', models.CharField(max_length=255, verbose_name='order_id')),
                ('status', models.CharField(max_length=255, verbose_name='status')),
                ('payment_id', models.CharField(max_length=255, null=True, verbose_name='invoice_id')),
                ('expire_by', models.CharField(max_length=255, verbose_name='expire_by')),
                ('issued_at', models.CharField(max_length=255, verbose_name='issued_at')),
                ('paid_at', models.CharField(max_length=255, null=True, verbose_name='paid_at')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('currency', models.CharField(max_length=255, verbose_name='currency')),
                ('short_url', models.CharField(max_length=255, verbose_name='short_url')),
                ('conference', models.PositiveIntegerField(default=0, verbose_name='conference')),
                ('user', models.PositiveIntegerField(default=0, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
