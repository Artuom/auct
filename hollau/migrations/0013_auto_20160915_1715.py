# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollau', '0012_auto_20160914_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='current_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u0442\u0435\u043a\u0443\u0449\u0430\u044f \u0446\u0435\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u043d\u0430\u0447\u0430\u043b\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0438'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='start_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u0441\u0442\u0430\u0440\u0442\u043e\u0432\u0430\u044f \u0446\u0435\u043d\u0430'),
        ),
    ]
