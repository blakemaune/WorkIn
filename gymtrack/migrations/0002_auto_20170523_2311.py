# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-24 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gymtrack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym_name', models.CharField(max_length=100)),
                ('workout_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(choices=[('Arms', (('armcurl', 'Biceps Curl'), ('armpress', 'Shoulder Press'))), ('Legs', (('legpress', 'Leg Press'), ('legcurl', 'Leg Curl'), ('legext', 'Leg Extension'))), ('Chest', (('chestpress', 'Chest Press'), ('chestfly', 'Chest Flys'))), ('unknown', 'Unknown')], max_length=100),
        ),
        migrations.AddField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(to='gymtrack.Exercise'),
        ),
    ]
