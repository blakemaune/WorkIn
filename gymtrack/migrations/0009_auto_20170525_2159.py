# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-26 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymtrack', '0008_auto_20170525_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
