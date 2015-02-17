# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0011_counttag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counttag',
            name='user',
            field=models.ForeignKey(related_name='user_click', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
