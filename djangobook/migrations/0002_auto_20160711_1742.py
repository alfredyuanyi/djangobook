# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-11 09:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangobook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
    ]
