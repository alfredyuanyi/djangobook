# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_delete_schoolnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
