# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-07 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialApp', '0005_auto_20171205_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='socialApp.Post'),
        ),
    ]
