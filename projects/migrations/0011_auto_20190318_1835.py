# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='projectsposted',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
