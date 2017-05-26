# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-24 04:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymtrack', '0003_auto_20170523_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(choices=[('Arms', (('armcurl', 'Biceps Curl'), ('armpress', 'Shoulder Press'))), ('Legs', (('legpress', 'Leg Press'), ('legcurl', 'Leg Curl'), ('legext', 'Leg Extension'))), ('Chest', (('chestpress', 'Chest Press'), ('chestfly', 'Chest Flys'))), ('cardio', 'Cardio Exercise'), ('unknown', 'Unknown')], max_length=100),
        ),
    ]
