# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='company_title',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job_title',
            field=models.CharField(max_length=255, verbose_name='job title', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age_group',
            field=models.CharField(max_length=255, choices=[('1', 'Less than 10'), ('2', '11-17'), ('3', '18-24'), ('4', '25-34'), ('5', '35-44'), ('6', '45 and over')], blank=True, verbose_name='age group', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(max_length=255, verbose_name='gender', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscribed',
            field=models.BooleanField(default=False, verbose_name='subscribed'),
        ),
    ]
