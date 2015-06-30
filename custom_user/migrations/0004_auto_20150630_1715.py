# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20150626_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivationprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 6, 30)),
        ),
    ]
