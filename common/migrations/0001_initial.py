# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('site', models.TextField(primary_key=True, serialize=False)),
                ('id', models.TextField()),
                ('pw', models.TextField()),
            ],
        ),
    ]
