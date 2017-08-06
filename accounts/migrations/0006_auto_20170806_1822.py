# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_timechecking'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_certified_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now(), verbose_name='인증시간'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_certified',
            field=models.BooleanField(default=False, verbose_name='인증여부'),
        ),
    ]
