# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_useractivationprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivationprofile',
            old_name='key_expies',
            new_name='key_expires',
        ),
    ]
