# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from shop.models import Goodsinfo,Goodsparameter
# Register your models here.
# 模型的管理器
@admin.register(Goodsinfo)
class GoodsinfoAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = (
        'id', 'goods_sn', 'name', 'add_time','market_price',
        'now_price','goods_brief','ship_free','is_hot'
    )

    # list_per_page设置每页显示多少条记录，默认是100条
    #list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    #ordering = ('-publish_time',)

    # list_editable 设置默认可编辑字段
    list_editable = [
        'name', 'market_price','now_price','ship_free','is_hot',
    ]

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('goods_sn', )

    # fk_fields 设置显示外键字段
    #fk_fields = ('machine_room_id',)

@admin.register(Goodsparameter)
class GoodsparameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods_sn', 'name', 'add_time','goods_num','goods_brand','goods_size','goods_color')
    list_editable = ['name','goods_num','goods_size','goods_color']
    list_display_links = ('goods_sn',)