# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtv', '0002_auto_20170529_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_favorite',
        ),
    ]
