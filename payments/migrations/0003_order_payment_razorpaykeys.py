# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20170806_0049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('order_id', models.CharField(max_length=255, verbose_name='order_id')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('currency', models.CharField(max_length=255, verbose_name='currency')),
                ('status', models.CharField(max_length=255, verbose_name='status')),
                ('created_at', models.CharField(max_length=255, null=True, verbose_name='created_at')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('payment_id', models.CharField(max_length=255, verbose_name='payment_id')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('currency', models.CharField(max_length=255, verbose_name='currency')),
                ('status', models.CharField(max_length=255, verbose_name='status')),
                ('order_id', models.CharField(max_length=255, verbose_name='order_id')),
                ('invoice_id', models.CharField(max_length=255, verbose_name='invoice_id')),
                ('international', models.BooleanField(default=False, db_index=True, verbose_name='international?')),
                ('amount_refunded', models.PositiveIntegerField(default=0, verbose_name='amount')),
                ('refund_status', models.CharField(max_length=255, verbose_name='refund_status')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('contact', models.CharField(max_length=15, null=True, verbose_name='contact', blank=True)),
                ('fee', models.PositiveIntegerField(default=0, verbose_name='fee')),
                ('service_tax', models.PositiveIntegerField(default=0, verbose_name='service_tax')),
                ('created_at', models.CharField(max_length=255, null=True, verbose_name='created_at')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RazorpayKeys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('api_key', models.CharField(max_length=255, verbose_name='order_id')),
                ('api_secret', models.CharField(max_length=255, verbose_name='order_id')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
