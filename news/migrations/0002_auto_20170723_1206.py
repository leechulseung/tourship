# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-23 12:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from accounts.models import Country, Local

country = Country.objects.get(id=1)
local = Local.objects.get(id='1')
class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170721_1850'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postprivacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.CharField(max_length=15, verbose_name='정책')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.TextField(default=' ', verbose_name='상세주소'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_posts', to='accounts.Country', verbose_name='국가'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='local',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_posts', to='accounts.Local', verbose_name='지역'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tourdate',
            field=models.CharField(default=datetime.datetime(2017, 7, 23, 12, 6, 9, 702999), max_length=15, verbose_name='여행날짜'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='privacy',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='news_posts', to='news.Postprivacy', verbose_name='Privacy related'),
            preserve_default=False,
        ),
    ]
