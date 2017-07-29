# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_conference', '0001_initial'),
        ('ticket', '0004_userticket_is_payment_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuxiliaryTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('title', models.CharField(max_length=255, verbose_name='name')),
                ('limit', models.PositiveIntegerField(default=0, verbose_name='limit')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description')),
                ('image_base64_title', models.CharField(max_length=255, null=True, verbose_name='image title', blank=True)),
                ('image_base64_text', models.TextField(null=True, verbose_name='image url', blank=True)),
                ('is_limit_reached', models.BooleanField(default=False, db_index=True, verbose_name='limit reached?')),
                ('disabled', models.BooleanField(default=False, db_index=True, verbose_name='disabled?')),
                ('conference', models.ForeignKey(verbose_name='conference', to='symposion_conference.Conference')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='userticket',
            name='auxiliary_ticket_id',
            field=models.CommaSeparatedIntegerField(default=0, max_length=200, verbose_name='auxiliary ticket'),
        ),
    ]
