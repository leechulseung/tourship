# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170806_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timechecking',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
    ]