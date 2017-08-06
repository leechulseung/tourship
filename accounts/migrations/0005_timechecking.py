# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170806_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timechecking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, verbose_name='시간')),
                ('token', models.CharField(max_length=10, verbose_name='토큰')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]