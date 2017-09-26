# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cauth', '0002_auto_20170722_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age_group',
            field=models.CharField(max_length=255, verbose_name='age group', choices=[(b'1', b'Less than 10'), (b'2', b'11-17'), (b'3', b'18-24'), (b'4', b'25-34'), (b'5', b'35-44'), (b'6', b'45 and over')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.CharField(max_length=255, verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact',
            field=models.CharField(max_length=15, verbose_name='contact'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='last name'),
        ),
    ]
