# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20180319_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='location_1',
            new_name='location',
        ),
    ]