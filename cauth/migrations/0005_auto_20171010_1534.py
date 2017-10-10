# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cauth', '0004_userprofile_tshirt_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tshirt_size',
            field=models.CharField(max_length=255, verbose_name='tshirt size', choices=[(b'MXS', b'Male: Xtra Small'), (b'MS', b'Male: Small'), (b'MM', b'Male: Medium'), (b'ML', b'Male: Large'), (b'MXL', b'Male: Xtra Large'), (b'MXXL', b'Male: Double Xtra Large'), (b'FXS', b'Female: Xtra Small'), (b'FS', b'Female: Small'), (b'FM', b'Female: Medium'), (b'FL', b'Female: Large'), (b'FXL', b'Female: Xtra Large'), (b'FXXL', b'Female: Double Xtra Large')]),
        ),
    ]
