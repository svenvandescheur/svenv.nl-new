# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-28 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codepenembed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='codepenembedplugin',
            name='user',
            field=models.CharField(default='svenvandescheur', max_length=255, verbose_name='Codepen user'),
            preserve_default=False,
        ),
    ]
