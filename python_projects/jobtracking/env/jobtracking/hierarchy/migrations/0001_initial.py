# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateTimeField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('userRequired', models.IntegerField(default=1)),
                ('description', models.TextField(default='Please Add Description', max_length=1000)),
                ('department', models.IntegerField(choices=[(1, 'School Education & Literacy'), (2, 'Higher Education'), (3, 'States/UTS')], default=1)),
                ('status', models.IntegerField(choices=[(1, 'Abandoned'), (2, 'Completed'), (3, 'Ongoing')], default=3)),
                ('skills', models.CharField(default='None', max_length=200)),
                ('difficulty', models.IntegerField(blank=True, default=1)),
                ('submitrequest', models.IntegerField(choices=[(1, 'On'), (2, 'Off')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hierarchy.Entity')),
            ],
            bases=('hierarchy.entity',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hierarchy.Entity')),
            ],
            bases=('hierarchy.entity',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hierarchy.Entity')),
                ('supervisorAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.Administrator')),
            ],
            bases=('hierarchy.entity',),
        ),
        migrations.AddField(
            model_name='job',
            name='jobemployee',
            field=models.ManyToManyField(to='hierarchy.Employee'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employeeSupervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.Supervisor'),
        ),
    ]
