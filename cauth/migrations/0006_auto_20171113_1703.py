# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cauth', '0005_auto_20171010_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age_group',
            field=models.CharField(max_length=255, choices=[('1', 'Less than 10'), ('2', '11-17'), ('3', '18-24'), ('4', '25-34'), ('5', '35-44'), ('6', '45 and over')], verbose_name='age group'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tshirt_size',
            field=models.CharField(max_length=255, choices=[('MXS', 'Male: Xtra Small'), ('MS', 'Male: Small'), ('MM', 'Male: Medium'), ('ML', 'Male: Large'), ('MXL', 'Male: Xtra Large'), ('MXXL', 'Male: Double Xtra Large'), ('FXS', 'Female: Xtra Small'), ('FS', 'Female: Small'), ('FM', 'Female: Medium'), ('FL', 'Female: Large'), ('FXL', 'Female: Xtra Large'), ('FXXL', 'Female: Double Xtra Large')], verbose_name='tshirt size'),
        ),
    ]
