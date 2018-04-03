# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_expense_location_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='location',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='location_category',
        ),
        migrations.AddField(
            model_name='expense',
            name='location_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expense', to='web.Location', verbose_name='Location'),
        ),
    ]