# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]