# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-21 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=50, verbose_name='상세주소'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.CharField(blank=True, max_length=120, verbose_name='생일'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=5, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_num',
            field=models.CharField(max_length=15, verbose_name='전화번호'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='local',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Local'),
            preserve_default=False,
        ),
    ]
