# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='license_plate',
            field=models.CharField(max_length=30),
        ),
    ]
