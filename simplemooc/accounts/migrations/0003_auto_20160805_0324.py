# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160805_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, default=True, max_length=100, verbose_name='Nome'),
        ),
    ]
