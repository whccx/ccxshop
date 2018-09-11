# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 15:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(default='', max_length=50, verbose_name='\u5546\u54c1\u552f\u4e00\u8d27\u53f7')),
                ('name', models.CharField(max_length=100, verbose_name='\u5546\u54c1\u540d')),
                ('goods_num', models.IntegerField(default=0, verbose_name='\u5e93\u5b58\u6570')),
                ('market_price', models.FloatField(default=0, verbose_name='\u5e02\u573a\u4ef7\u683c')),
                ('now_price', models.FloatField(default=0, verbose_name='\u73b0\u552e\u4ef7\u683c')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='\u5546\u54c1\u7b80\u77ed\u63cf\u8ff0')),
                ('ship_free', models.BooleanField(default=True, verbose_name='\u662f\u5426\u5305\u90ae')),
                ('is_hot', models.BooleanField(default=False, verbose_name='\u662f\u5426\u70ed\u9500')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'ordering': ('goods_sn',),
                'verbose_name': '\u5546\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u5546\u54c1\u4fe1\u606f',
            },
        ),
    ]
