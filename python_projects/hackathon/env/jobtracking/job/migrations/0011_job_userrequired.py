# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_auto_20170401_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='userRequired',
            field=models.IntegerField(default=1),
        ),
    ]