# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-28 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepenembed', '0004_codepenembedplugin_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='codepenembedplugin',
            name='theme_id',
            field=models.IntegerField(default=0, max_length=b'5', verbose_name='Theme id'),
        ),
    ]
