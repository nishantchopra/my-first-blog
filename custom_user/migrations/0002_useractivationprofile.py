# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(blank=True, max_length=40)),
                ('key_expies', models.DateTimeField(default=datetime.date(2015, 6, 26))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
