# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
