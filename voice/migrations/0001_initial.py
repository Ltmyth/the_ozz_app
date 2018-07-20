# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fwno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.CharField(max_length=13)),
            ],
        ),
    ]
