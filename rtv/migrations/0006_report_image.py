# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rtv', '0005_auto_20170529_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
