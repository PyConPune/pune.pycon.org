# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('symposion_conference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(max_length=255, verbose_name='gender')),
                ('size', models.CharField(max_length=5, verbose_name='size')),
                ('limit', models.PositiveIntegerField(default=0, verbose_name='limit')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price', db_index=True)),
                ('conference', models.ForeignKey(verbose_name='conference', to='symposion_conference.Conference')),
            ],
            options={
                'verbose_name': 'tshirt',
                'verbose_name_plural': 'tshirts',
            },
        ),
        migrations.CreateModel(
            name='UserTshirt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('tshirt', models.ForeignKey(to='inventory.Tshirt')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'user tshirt',
                'verbose_name_plural': 'tshirt',
            },
        ),
    ]
