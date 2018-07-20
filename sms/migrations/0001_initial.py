# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('message', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Smshist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
                ('content', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=25)),
                ('destination', models.CharField(max_length=255)),
            ],
        ),
    ]
