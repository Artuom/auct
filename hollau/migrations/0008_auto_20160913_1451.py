# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollau', '0007_auto_20160913_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u043d\u0430\u0447\u0430\u043b\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0438'),
        ),
    ]