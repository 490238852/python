# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-15 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
