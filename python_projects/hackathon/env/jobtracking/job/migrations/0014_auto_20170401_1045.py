# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_auto_20170401_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='joblevel',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'User')], default=1),
        ),
    ]