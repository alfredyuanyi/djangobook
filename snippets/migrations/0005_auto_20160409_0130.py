# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 01:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20160326_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchId', models.IntegerField(default=0)),
                ('branchName', models.CharField(default='unNamedBranch', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='snippets.User')),
                ('topNewsTime', models.DateTimeField()),
                ('bottomNewsTime', models.DateTimeField()),
                ('concernedDirection', models.CharField(default='000000', max_length=100)),
            ],
            bases=('snippets.user',),
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('creatTime',)},
        ),
        migrations.AlterField(
            model_name='concerndirection',
            name='officeOfTeachingAffairs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='concerndirection',
            name='personnelDivision',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='concerndirection',
            name='schoolOfComputing',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=150),
        ),
    ]
