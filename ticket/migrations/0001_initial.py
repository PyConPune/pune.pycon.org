# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('symposion_conference', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('code', models.CharField(verbose_name='coupon', max_length=20)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('title', models.CharField(verbose_name='name', max_length=255)),
                ('limit', models.PositiveIntegerField(default=0, verbose_name='limit')),
                ('price', models.PositiveIntegerField(db_index=True, default=0, verbose_name='price')),
                ('description', models.CharField(null=True, verbose_name='description', max_length=255)),
                ('conference', models.ForeignKey(to='symposion_conference.Conference', verbose_name='conference')),
            ],
            options={
                'verbose_name_plural': 'tickets',
                'verbose_name': 'ticket',
            },
        ),
        migrations.CreateModel(
            name='TicketAddons',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('title', models.CharField(verbose_name='name', max_length=255)),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('ticket', models.ForeignKey(to='ticket.Ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('ticket', models.ForeignKey(to='ticket.Ticket')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'user tickets',
                'verbose_name': 'user ticket',
                'ordering': ['-timestamp'],
            },
        ),
    ]
