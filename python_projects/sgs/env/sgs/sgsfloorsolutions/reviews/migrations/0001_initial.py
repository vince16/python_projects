# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]