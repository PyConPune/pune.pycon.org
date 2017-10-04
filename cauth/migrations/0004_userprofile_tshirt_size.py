# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cauth', '0003_auto_20170926_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tshirt_size',
            field=models.CharField(default=datetime.datetime(2017, 10, 4, 15, 16, 20, 426033, tzinfo=utc), max_length=255, verbose_name='tshirt size', choices=[(b'XS', b'Xtra Small'), (b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'Xtra Large'), (b'XXL', b'Double Xtra Large')]),
            preserve_default=False,
        ),
    ]
