# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='goods_img',
            field=models.ImageField(upload_to='media/upload', verbose_name='\u5546\u54c1\u56fe\u7247'),
        ),
    ]
