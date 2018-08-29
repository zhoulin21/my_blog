# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180821_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tagname',
            new_name='tag_name',
        ),
    ]
