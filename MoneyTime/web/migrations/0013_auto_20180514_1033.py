# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-14 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_prediction_predicted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='applied',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Applied'),
        ),
    ]
