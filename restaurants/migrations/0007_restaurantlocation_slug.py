# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-12-24 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20191222_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
