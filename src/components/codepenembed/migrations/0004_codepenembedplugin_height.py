# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-28 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepenembed', '0003_auto_20161128_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='codepenembedplugin',
            name='height',
            field=models.IntegerField(default=480, verbose_name='Height'),
        ),
    ]
