# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]