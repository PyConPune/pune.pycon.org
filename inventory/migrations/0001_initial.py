# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('symposion_conference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('gender', models.CharField(verbose_name='gender', max_length=255)),
                ('size', models.CharField(verbose_name='size', max_length=5)),
                ('limit', models.PositiveIntegerField(default=0, verbose_name='limit')),
                ('price', models.PositiveIntegerField(db_index=True, default=0, verbose_name='price')),
                ('conference', models.ForeignKey(to='symposion_conference.Conference', verbose_name='conference')),
            ],
            options={
                'verbose_name_plural': 'tshirts',
                'verbose_name': 'tshirt',
            },
        ),
        migrations.CreateModel(
            name='UserTshirt',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('tshirt', models.ForeignKey(to='inventory.Tshirt')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'tshirt',
                'verbose_name': 'user tshirt',
                'ordering': ['-timestamp'],
            },
        ),
    ]
