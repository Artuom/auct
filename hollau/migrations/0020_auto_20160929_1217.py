# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-29 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollau', '0019_auto_20160928_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phonenumber',
            field=models.CharField(default=None, max_length=20, null=True, verbose_name='\u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='userlocation',
            field=models.CharField(default=None, max_length=100, verbose_name='\u043c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.TextField(null=True),
        ),
    ]
