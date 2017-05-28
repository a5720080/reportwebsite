# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('license_plate', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rtv.Report'),
        ),
    ]